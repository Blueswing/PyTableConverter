# Generated from JSONTable.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\5\2\21\n\2\3\3\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3\32")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\"\n\3\f\3\16\3%\13\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3+\n\3\3\4\3\4\3\4\3\4\7\4\61\n\4\f")
        buf.write("\4\16\4\64\13\4\3\4\3\4\3\4\3\4\5\4:\n\4\3\5\3\5\3\5\3")
        buf.write("\5\7\5@\n\5\f\5\16\5C\13\5\3\5\3\5\3\5\3\5\5\5I\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\t")
        buf.write("\16\2S\2\16\3\2\2\2\4*\3\2\2\2\69\3\2\2\2\bH\3\2\2\2\n")
        buf.write("J\3\2\2\2\fN\3\2\2\2\16\20\5\4\3\2\17\21\7\2\2\3\20\17")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\3\3\2\2\2\22\23\7\3\2\2\23\30")
        buf.write("\5\6\4\2\24\25\7\4\2\2\25\27\5\6\4\2\26\24\3\2\2\2\27")
        buf.write("\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\33\3\2\2\2")
        buf.write("\32\30\3\2\2\2\33\34\7\5\2\2\34+\3\2\2\2\35\36\7\3\2\2")
        buf.write("\36#\5\b\5\2\37 \7\4\2\2 \"\5\b\5\2!\37\3\2\2\2\"%\3\2")
        buf.write("\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%#\3\2\2\2&\'\7\5\2")
        buf.write("\2\'+\3\2\2\2()\7\3\2\2)+\7\5\2\2*\22\3\2\2\2*\35\3\2")
        buf.write("\2\2*(\3\2\2\2+\5\3\2\2\2,-\7\6\2\2-\62\5\n\6\2./\7\4")
        buf.write("\2\2/\61\5\n\6\2\60.\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2")
        buf.write("\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65\66\7\7")
        buf.write("\2\2\66:\3\2\2\2\678\7\6\2\28:\7\7\2\29,\3\2\2\29\67\3")
        buf.write("\2\2\2:\7\3\2\2\2;<\7\3\2\2<A\5\f\7\2=>\7\4\2\2>@\5\f")
        buf.write("\7\2?=\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2")
        buf.write("CA\3\2\2\2DE\7\5\2\2EI\3\2\2\2FG\7\3\2\2GI\7\5\2\2H;\3")
        buf.write("\2\2\2HF\3\2\2\2I\t\3\2\2\2JK\7\f\2\2KL\7\b\2\2LM\5\f")
        buf.write("\7\2M\13\3\2\2\2NO\t\2\2\2O\r\3\2\2\2\n\20\30#*\629AH")
        return buf.getvalue()


class JSONTableParser ( Parser ):

    grammarFileName = "JSONTable.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "'{'", "'}'", "':'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TRUE", "FALSE", 
                      "NULL", "STRING", "FLOAT", "INT", "WS" ]

    RULE_table = 0
    RULE_arr = 1
    RULE_simpleObj = 2
    RULE_simpleArr = 3
    RULE_pair = 4
    RULE_simpleValue = 5

    ruleNames =  [ "table", "arr", "simpleObj", "simpleArr", "pair", "simpleValue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    TRUE=7
    FALSE=8
    NULL=9
    STRING=10
    FLOAT=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr(self):
            return self.getTypedRuleContext(JSONTableParser.ArrContext,0)


        def EOF(self):
            return self.getToken(JSONTableParser.EOF, 0)

        def getRuleIndex(self):
            return JSONTableParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = JSONTableParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.arr()
            self.state = 14
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 13
                self.match(JSONTableParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONTableParser.RULE_arr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ObjTableContext(ArrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONTableParser.ArrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simpleObj(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONTableParser.SimpleObjContext)
            else:
                return self.getTypedRuleContext(JSONTableParser.SimpleObjContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjTable" ):
                listener.enterObjTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjTable" ):
                listener.exitObjTable(self)


    class ArrTableContext(ArrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONTableParser.ArrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simpleArr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONTableParser.SimpleArrContext)
            else:
                return self.getTypedRuleContext(JSONTableParser.SimpleArrContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrTable" ):
                listener.enterArrTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrTable" ):
                listener.exitArrTable(self)



    def arr(self):

        localctx = JSONTableParser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arr)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = JSONTableParser.ObjTableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(JSONTableParser.T__0)
                self.state = 17
                self.simpleObj()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 18
                    self.match(JSONTableParser.T__1)
                    self.state = 19
                    self.simpleObj()
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.match(JSONTableParser.T__2)
                pass

            elif la_ == 2:
                localctx = JSONTableParser.ArrTableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(JSONTableParser.T__0)
                self.state = 28
                self.simpleArr()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 29
                    self.match(JSONTableParser.T__1)
                    self.state = 30
                    self.simpleArr()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(JSONTableParser.T__2)
                pass

            elif la_ == 3:
                localctx = JSONTableParser.ArrTableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.match(JSONTableParser.T__0)
                self.state = 39
                self.match(JSONTableParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONTableParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONTableParser.PairContext,i)


        def getRuleIndex(self):
            return JSONTableParser.RULE_simpleObj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleObj" ):
                listener.enterSimpleObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleObj" ):
                listener.exitSimpleObj(self)




    def simpleObj(self):

        localctx = JSONTableParser.SimpleObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simpleObj)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(JSONTableParser.T__3)
                self.state = 43
                self.pair()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 44
                    self.match(JSONTableParser.T__1)
                    self.state = 45
                    self.pair()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self.match(JSONTableParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(JSONTableParser.T__3)
                self.state = 54
                self.match(JSONTableParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleArrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONTableParser.SimpleValueContext)
            else:
                return self.getTypedRuleContext(JSONTableParser.SimpleValueContext,i)


        def getRuleIndex(self):
            return JSONTableParser.RULE_simpleArr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleArr" ):
                listener.enterSimpleArr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleArr" ):
                listener.exitSimpleArr(self)




    def simpleArr(self):

        localctx = JSONTableParser.SimpleArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simpleArr)
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(JSONTableParser.T__0)
                self.state = 58
                self.simpleValue()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 59
                    self.match(JSONTableParser.T__1)
                    self.state = 60
                    self.simpleValue()
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self.match(JSONTableParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(JSONTableParser.T__0)
                self.state = 69
                self.match(JSONTableParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONTableParser.STRING, 0)

        def simpleValue(self):
            return self.getTypedRuleContext(JSONTableParser.SimpleValueContext,0)


        def getRuleIndex(self):
            return JSONTableParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = JSONTableParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(JSONTableParser.STRING)
            self.state = 73
            self.match(JSONTableParser.T__5)
            self.state = 74
            self.simpleValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONTableParser.STRING, 0)

        def INT(self):
            return self.getToken(JSONTableParser.INT, 0)

        def FLOAT(self):
            return self.getToken(JSONTableParser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(JSONTableParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(JSONTableParser.FALSE, 0)

        def NULL(self):
            return self.getToken(JSONTableParser.NULL, 0)

        def getRuleIndex(self):
            return JSONTableParser.RULE_simpleValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleValue" ):
                listener.enterSimpleValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleValue" ):
                listener.exitSimpleValue(self)




    def simpleValue(self):

        localctx = JSONTableParser.SimpleValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_simpleValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONTableParser.TRUE) | (1 << JSONTableParser.FALSE) | (1 << JSONTableParser.NULL) | (1 << JSONTableParser.STRING) | (1 << JSONTableParser.FLOAT) | (1 << JSONTableParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





