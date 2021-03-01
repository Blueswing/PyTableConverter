# Generated from MarkdownTable.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(",\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\5\3\21\n\3\3\3\6\3\24\n\3\r\3\16\3\25\3\3\5\3\31")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\6\4 \n\4\r\4\16\4!\3\5\5\5%\n")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7")
        buf.write("\3\2\4\6\2\f\f\17\17^^~~\5\2\13\f\17\17\"\"\2\62\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\3\r\3\2\2\2\5\20\3\2\2\2\7\37\3\2\2\2\t$\3\2\2\2\13")
        buf.write("(\3\2\2\2\r\16\7~\2\2\16\4\3\2\2\2\17\21\7<\2\2\20\17")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\23\3\2\2\2\22\24\7/\2\2\23\22")
        buf.write("\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\30\3\2\2\2\27\31\7<\2\2\30\27\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\6\3\2\2\2\32\33\7^\2\2\33 \7^\2\2\34\35\7^\2\2\35 \7")
        buf.write("~\2\2\36 \n\2\2\2\37\32\3\2\2\2\37\34\3\2\2\2\37\36\3")
        buf.write("\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\b\3\2\2\2#%")
        buf.write("\7\17\2\2$#\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\7\f\2\2\'\n")
        buf.write("\3\2\2\2()\t\3\2\2)*\3\2\2\2*+\b\6\2\2+\f\3\2\2\2\t\2")
        buf.write("\20\25\30\37!$\3\b\2\2")
        return buf.getvalue()


class MarkdownTableLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BAR = 2
    STRING = 3
    NL = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'" ]

    symbolicNames = [ "<INVALID>",
            "BAR", "STRING", "NL", "WS" ]

    ruleNames = [ "T__0", "BAR", "STRING", "NL", "WS" ]

    grammarFileName = "MarkdownTable.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


