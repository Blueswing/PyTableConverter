# Generated from CSV.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("#\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\6\5\25\n\5\r\5\16\5\26\3\6\3\6\3")
        buf.write("\6\3\6\7\6\35\n\6\f\6\16\6 \13\6\3\6\3\6\2\2\7\3\3\5\4")
        buf.write("\7\5\t\6\13\7\3\2\4\6\2\f\f\17\17$$..\3\2$$\2%\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\3\r\3\2\2\2\5\17\3\2\2\2\7\21\3\2\2\2\t\24\3\2\2\2\13")
        buf.write("\30\3\2\2\2\r\16\7.\2\2\16\4\3\2\2\2\17\20\7\17\2\2\20")
        buf.write("\6\3\2\2\2\21\22\7\f\2\2\22\b\3\2\2\2\23\25\n\2\2\2\24")
        buf.write("\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2")
        buf.write("\27\n\3\2\2\2\30\36\7$\2\2\31\32\7$\2\2\32\35\7$\2\2\33")
        buf.write("\35\n\3\2\2\34\31\3\2\2\2\34\33\3\2\2\2\35 \3\2\2\2\36")
        buf.write("\34\3\2\2\2\36\37\3\2\2\2\37!\3\2\2\2 \36\3\2\2\2!\"\7")
        buf.write("$\2\2\"\f\3\2\2\2\6\2\26\34\36\2")
        return buf.getvalue()


class CSVLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    TEXT = 4
    STRING = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'\r'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "TEXT", "STRING" ]

    grammarFileName = "CSV.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


