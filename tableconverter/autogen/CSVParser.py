# Generated from CSV.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\5\2\27\n\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\7\4\36\n\4\f\4\16\4!\13\4\3\5\3\5\3\5")
        buf.write("\5\5&\n\5\3\5\2\2\6\2\4\6\b\2\2\2)\2\n\3\2\2\2\4\30\3")
        buf.write("\2\2\2\6\32\3\2\2\2\b%\3\2\2\2\n\22\5\4\3\2\13\r\7\3\2")
        buf.write("\2\f\13\3\2\2\2\f\r\3\2\2\2\r\16\3\2\2\2\16\17\7\4\2\2")
        buf.write("\17\21\5\6\4\2\20\f\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\25\27\7\2")
        buf.write("\2\3\26\25\3\2\2\2\26\27\3\2\2\2\27\3\3\2\2\2\30\31\5")
        buf.write("\6\4\2\31\5\3\2\2\2\32\37\5\b\5\2\33\34\7\5\2\2\34\36")
        buf.write("\5\b\5\2\35\33\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3")
        buf.write("\2\2\2 \7\3\2\2\2!\37\3\2\2\2\"&\7\6\2\2#&\7\7\2\2$&\3")
        buf.write("\2\2\2%\"\3\2\2\2%#\3\2\2\2%$\3\2\2\2&\t\3\2\2\2\7\f\22")
        buf.write("\26\37%")
        return buf.getvalue()


class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\r'", "'\n'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "STRING" ]

    RULE_fil = 0
    RULE_hdr = 1
    RULE_row = 2
    RULE_field = 3

    ruleNames =  [ "fil", "hdr", "row", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TEXT=4
    STRING=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FilContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hdr(self):
            return self.getTypedRuleContext(CSVParser.HdrContext,0)


        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def EOF(self):
            return self.getToken(CSVParser.EOF, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_fil

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFil" ):
                listener.enterFil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFil" ):
                listener.exitFil(self)




    def fil(self):

        localctx = CSVParser.FilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_fil)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.hdr()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSVParser.T__0 or _la==CSVParser.T__1:
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSVParser.T__0:
                    self.state = 9
                    self.match(CSVParser.T__0)


                self.state = 12
                self.match(CSVParser.T__1)
                self.state = 13
                self.row()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 19
                self.match(CSVParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HdrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(CSVParser.RowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_hdr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHdr" ):
                listener.enterHdr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHdr" ):
                listener.exitHdr(self)




    def hdr(self):

        localctx = CSVParser.HdrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hdr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.row()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.field()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSVParser.T__2:
                self.state = 25
                self.match(CSVParser.T__2)
                self.state = 26
                self.field()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVParser.RULE_field

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class TextContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)


    class EmptyContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)



    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSVParser.TEXT]:
                localctx = CSVParser.TextContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(CSVParser.TEXT)
                pass
            elif token in [CSVParser.STRING]:
                localctx = CSVParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(CSVParser.STRING)
                pass
            elif token in [CSVParser.EOF, CSVParser.T__0, CSVParser.T__1, CSVParser.T__2]:
                localctx = CSVParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





