# Generated from MarkdownTable.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(")\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\4\5\4\23\n\4\3\4\6\4\26\n\4\r\4\16\4\27\3\4")
        buf.write("\5\4\33\n\4\3\5\3\5\3\5\3\5\3\5\6\5\"\n\5\r\5\16\5#\3")
        buf.write("\6\3\6\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\4\4\2^^")
        buf.write("~~\5\2\13\f\17\17\"\"\2.\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2")
        buf.write("\2\7\22\3\2\2\2\t!\3\2\2\2\13%\3\2\2\2\r\16\7\f\2\2\16")
        buf.write("\4\3\2\2\2\17\20\7~\2\2\20\6\3\2\2\2\21\23\7<\2\2\22\21")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\25\3\2\2\2\24\26\7/\2\2\25\24")
        buf.write("\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\32\3\2\2\2\31\33\7<\2\2\32\31\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\b\3\2\2\2\34\35\7^\2\2\35\"\7^\2\2\36\37\7^\2\2\37\"")
        buf.write("\7~\2\2 \"\n\2\2\2!\34\3\2\2\2!\36\3\2\2\2! \3\2\2\2\"")
        buf.write("#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\n\3\2\2\2%&\t\3\2\2&\'")
        buf.write("\3\2\2\2\'(\b\6\2\2(\f\3\2\2\2\b\2\22\27\32!#\3\b\2\2")
        return buf.getvalue()


class MarkdownTableLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BAR = 3
    STRING = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "BAR", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "BAR", "STRING", "WS" ]

    grammarFileName = "MarkdownTable.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


