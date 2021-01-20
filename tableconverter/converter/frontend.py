import re
from typing import Dict
from collections import deque
from antlr4 import TokenStream, CommonTokenStream, Parser, Lexer
from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import ParseTree, ParseTreeListener, ParseTreeWalker
from ..autogen.CSVLexer import CSVLexer
from ..autogen.CSVParser import CSVParser
from ..autogen.CSVListener import CSVListener
from ..autogen.JSONTableLexer import JSONTableLexer
from ..autogen.JSONTableParser import JSONTableParser
from ..autogen.JSONTableListener import JSONTableListener
from ..autogen.MarkdownTableLexer import MarkdownTableLexer
from ..autogen.MarkdownTableParser import MarkdownTableParser
from ..autogen.MarkdownTableListener import MarkdownTableListener
from ..autogen.HTMLLexer import HTMLLexer
from ..autogen.HTMLTable import HTMLTable
from ..autogen.HTMLTableListener import HTMLTableListener
from ..model import Table
from ..util import REVERSE_ENTITY_MAP


class SourceSyntaxError(Exception):
    pass


class ExceptionalErrorListener(ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        err = "line " + str(line) + ":" + str(column) + " " + msg
        raise SourceSyntaxError(err)


class AbstractTableConverter(ParseTreeListener):
    def get_result(self) -> Table:
        raise NotImplementedError()


class AbstractFrontend:
    def __init__(self):
        self._walker = ParseTreeWalker()

    def _get_tree(self, in_stream: InputStream):
        raise NotImplementedError()

    def _get_converter(self) -> AbstractTableConverter:
        raise NotImplementedError()

    def get_ir(self, in_stream: InputStream) -> Table:
        tree = self._get_tree(in_stream)
        converter = self._get_converter()
        self._walker.walk(converter, tree)
        return converter.get_result()


class AbstractParseTreeFactory:
    def __init__(self) -> None:
        self._error_listener = ExceptionalErrorListener()

    def get_lexer(self, in_stream: InputStream) -> Lexer:
        lexer = self._get_lexer(in_stream)
        self._change_error_listener(lexer)
        return lexer

    def get_parser(self, in_stream: InputStream) -> Parser:
        lexer = self.get_lexer(in_stream)
        token_stream = CommonTokenStream(lexer)
        parser = self._get_parser(token_stream)
        self._change_error_listener(parser)
        return parser

    def _change_error_listener(self, recog) -> None:
        recog.removeErrorListeners()
        recog.addErrorListener(self._error_listener)

    def _get_lexer(self, in_stream: InputStream) -> Lexer:
        raise NotImplementedError()

    def _get_parser(self, token_stream: TokenStream) -> Parser:
        raise NotImplementedError()

    def get_tree(self, in_stream: InputStream) -> ParseTree:
        raise NotImplementedError()


class CSVParseTreeFactory(AbstractParseTreeFactory):
    def _get_lexer(self, in_stream: InputStream) -> Lexer:
        return CSVLexer(in_stream)

    def _get_parser(self, token_stream: TokenStream) -> Parser:
        return CSVParser(token_stream)

    def get_tree(self, in_stream: InputStream) -> ParseTree:
        return self.get_parser(in_stream).fil()


class BaseFrontend(AbstractFrontend):
    def _get_lexer(self, in_stream: InputStream) -> Lexer:
        raise NotImplementedError()

    def _get_parser(self: TokenStream) -> Parser:
        raise NotImplementedError()

    def _get_tree(self, in_stream: InputStream):
        lexer = self._get_lexer(in_stream)
        token_stream = CommonTokenStream(lexer)
        parser = self._get_parser(token_stream)
        parser.removeErrorListeners()


class JSONTableConverter(AbstractTableConverter, JSONTableListener):
    def __init__(self):
        self._table_obj = Table([])
        self._is_arr = False
        self._in_header = True
        self._cur_row = []
        self._key_index_map = {}  # type: Dict[str, int]

    def exitSimpleArr(self, ctx: JSONTableParser.SimpleArrContext):
        if self._in_header:
            self._in_header = False
            self._table_obj.header = self._cur_row
        else:
            self._table_obj.add_row(self._cur_row)
        self._cur_row = []

    def exitSimpleObj(self, ctx: JSONTableParser.SimpleObjContext):
        self._table_obj.add_row(self._cur_row)
        self._cur_row = [None] * len(self._key_index_map)

    def enterArrTable(self, ctx: JSONTableParser.ArrTableContext):
        self._is_arr = True

    def enterSimpleValue(self, ctx: JSONTableParser.SimpleValueContext):
        if self._is_arr:
            v = self._eval_value(ctx)
            self._cur_row.append(v)

    def enterPair(self, ctx: JSONTableParser.PairContext):
        key = self._process_string_context(ctx.STRING())
        val = self._eval_value(ctx.simpleValue())
        if key in self._key_index_map:
            idx = self._key_index_map[key]
        else:
            idx = len(self._table_obj.header)
            self._key_index_map[key] = idx
            self._table_obj.header.append(key)
            for r in self._table_obj.body:
                r.append(None)
            self._cur_row.append(None)
        self._cur_row[idx] = val

    def get_result(self) -> Table:
        return self._table_obj

    @classmethod
    def _eval_value(cls, ctx):
        v = ctx.STRING()
        if v is not None:
            return cls._process_string_context(v)
        v = ctx.INT()
        if v is not None:
            return int(v.getText())
        v = ctx.FLOAT()
        if v is not None:
            return float(v.getText())
        v = ctx.TRUE()
        if v is not None:
            return True
        v = ctx.FALSE()
        if v is not None:
            return False
        v = ctx.NULL()
        if v is not None:
            return None
        return ""

    @classmethod
    def _process_string_context(cls, ctx):
        return ctx.getText()[1:-1].encode("utf8").decode("unicode-escape")


class JSONTableFrontend(AbstractFrontend):
    def _get_converter(self) -> AbstractTableConverter:
        return JSONTableConverter()

    def _get_tree(self, in_stream: InputStream):
        lexer = JSONTableLexer(in_stream)
        token_stream = CommonTokenStream(lexer)
        parser = JSONTableParser(token_stream)
        return parser.table()


class CSVConverter(AbstractTableConverter, CSVListener):
    def __init__(self) -> None:
        self._in_header = False
        self._table_obj = Table()
        self._cur_row = []

    def get_result(self) -> Table:
        return self._table_obj

    def exitRow(self, ctx: CSVParser.RowContext):
        if self._in_header:
            self._table_obj.header = self._cur_row
        else:
            self._table_obj.add_row(self._cur_row)
        self._cur_row = []

    def enterHdr(self, ctx: CSVParser.HdrContext):
        self._in_header = True

    def exitHdr(self, ctx: CSVParser.HdrContext):
        self._in_header = False

    def exitEmpty(self, ctx: CSVParser.EmptyContext):
        self._cur_row.append("")

    def exitString(self, ctx: CSVParser.StringContext):
        self._cur_row.append(ctx.getText()[1:-1].replace('""', '"'))

    def exitText(self, ctx: CSVParser.TextContext):
        self._cur_row.append(ctx.getText())


class CSVFrontend(AbstractFrontend):
    def _get_converter(self) -> AbstractTableConverter:
        return CSVConverter()

    def _get_tree(self, in_stream: InputStream):
        factory = CSVParseTreeFactory()
        return factory.get_tree(in_stream)


class MarkdownTableConverter(AbstractTableConverter, MarkdownTableListener):
    def __init__(self) -> None:
        super().__init__()
        self._in_header = False
        self._table_obj = Table()
        self._cur_row = []

    def exitRow(self, ctx: MarkdownTableParser.RowContext):
        if self._in_header:
            self._table_obj.header = self._cur_row
        else:
            self._table_obj.add_row(self._cur_row)
        self._cur_row = []

    def enterItem(self, ctx: MarkdownTableParser.ItemContext):
        self._cur_row.append(ctx.getText().replace("\\\\", "\\").replace("\\|", "|"))

    def enterHeader(self, ctx: MarkdownTableParser.HeaderContext):
        self._in_header = True

    def exitHeader(self, ctx: MarkdownTableParser.HeaderContext):
        self._in_header = False

    def get_result(self) -> Table:
        return self._table_obj


class MarkdownTableFrontend(AbstractFrontend):
    def _get_tree(self, in_stream: InputStream):
        lexer = MarkdownTableLexer(in_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MarkdownTableParser(token_stream)
        return parser.table()

    def _get_converter(self) -> AbstractTableConverter:
        return MarkdownTableConverter()


class HTMLTableConverter(AbstractTableConverter, HTMLTableListener):
    _RE_HTML_ENTITY = re.compile(r"&[a-zA-Z]+?;")

    _TABLE_TAGS = {"tr", "th", "td"}

    def __init__(self):
        super().__init__()
        self._table_obj = Table()
        self._cur_row = []
        self._tag_stack = deque()
        self._in_header = False

    def get_result(self) -> Table:
        return self._table_obj

    @property
    def _cur_tag(self):
        if len(self._tag_stack) == 0:
            return None
        return self._tag_stack[-1]

    def enterNormalTag(self, ctx: HTMLTable.NormalTagContext):
        tag = ctx.tag.text
        self._tag_stack.append(tag)
        if tag == "th":
            self._in_header |= True
            cell = self._process_content(ctx.content)
            self._cur_row.append(cell)
        elif tag == "td":
            cell = self._process_content(ctx.content)
            self._cur_row.append(cell)

    def exitNormalTag(self, ctx: HTMLTable.NormalTagContext):
        tag = self._tag_stack.pop()
        if tag == "tr":
            if self._in_header:
                self._in_header = False
                if self._table_obj.header is None:
                    self._table_obj.header = self._cur_row

                else:
                    raise Exception("multiple header rows")
            else:
                self._table_obj.add_row(self._cur_row)
            self._cur_row = []

    @classmethod
    def _process_content(cls, content):
        if content is None:
            cell_text = ""
        else:
            cell_text = content.getText()
        return cls._clean_html_text(cell_text)

    @classmethod
    def _clean_html_text(cls, html_data):
        return re.sub(cls._RE_HTML_ENTITY, cls.replace_func, html_data)

    @classmethod
    def replace_func(cls, match_obj: "re.Match"):
        raw = match_obj.group(0)
        return REVERSE_ENTITY_MAP.get(raw, raw)


class HTMLTableFrontend(AbstractFrontend):
    def _get_tree(self, in_stream: InputStream):
        lexer = HTMLLexer(in_stream)
        token_stream = CommonTokenStream(lexer)
        parser = HTMLTable(token_stream)
        return parser.table()

    def _get_converter(self) -> AbstractTableConverter:
        return HTMLTableConverter()


class FrontendFactory:
    _FRONTEND_MAP = {
        "csv": CSVFrontend,
        "json": JSONTableFrontend,
        "md": MarkdownTableFrontend,
        "html": HTMLTableFrontend,
    }  # type: Dict[str, AbstractFrontend]

    @classmethod
    def new_instance(cls, fmt) -> AbstractFrontend:
        if fmt in cls._FRONTEND_MAP:
            clz = cls._FRONTEND_MAP[fmt]
            return clz()
        raise ValueError("{} frontend is not supported".format(fmt))
