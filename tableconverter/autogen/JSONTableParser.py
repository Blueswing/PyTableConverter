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
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3*\n\3\3\4\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4")
        buf.write("\63\13\4\3\4\3\4\3\4\3\4\5\49\n\4\3\5\3\5\3\5\3\5\7\5")
        buf.write("?\n\5\f\5\16\5B\13\5\3\5\3\5\3\5\3\5\5\5H\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\t\16\2")
        buf.write("Q\2\16\3\2\2\2\4)\3\2\2\2\68\3\2\2\2\bG\3\2\2\2\nI\3\2")
        buf.write("\2\2\fM\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2")
        buf.write("\2\21\22\7\3\2\2\22\27\5\6\4\2\23\24\7\4\2\2\24\26\5\6")
        buf.write("\4\2\25\23\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3")
        buf.write("\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33\7\5\2\2\33*\3")
        buf.write("\2\2\2\34\35\7\3\2\2\35\"\5\b\5\2\36\37\7\4\2\2\37!\5")
        buf.write("\b\5\2 \36\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3")
        buf.write("\2\2\2$\"\3\2\2\2%&\7\5\2\2&*\3\2\2\2\'(\7\3\2\2(*\7\5")
        buf.write("\2\2)\21\3\2\2\2)\34\3\2\2\2)\'\3\2\2\2*\5\3\2\2\2+,\7")
        buf.write("\6\2\2,\61\5\n\6\2-.\7\4\2\2.\60\5\n\6\2/-\3\2\2\2\60")
        buf.write("\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\64\3\2\2\2\63")
        buf.write("\61\3\2\2\2\64\65\7\7\2\2\659\3\2\2\2\66\67\7\6\2\2\67")
        buf.write("9\7\7\2\28+\3\2\2\28\66\3\2\2\29\7\3\2\2\2:;\7\3\2\2;")
        buf.write("@\5\f\7\2<=\7\4\2\2=?\5\f\7\2><\3\2\2\2?B\3\2\2\2@>\3")
        buf.write("\2\2\2@A\3\2\2\2AC\3\2\2\2B@\3\2\2\2CD\7\5\2\2DH\3\2\2")
        buf.write("\2EF\7\3\2\2FH\7\5\2\2G:\3\2\2\2GE\3\2\2\2H\t\3\2\2\2")
        buf.write("IJ\7\f\2\2JK\7\b\2\2KL\5\f\7\2L\13\3\2\2\2MN\t\2\2\2N")
        buf.write("\r\3\2\2\2\t\27\")\618@G")
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
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = JSONTableParser.ObjTableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(JSONTableParser.T__0)
                self.state = 16
                self.simpleObj()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 17
                    self.match(JSONTableParser.T__1)
                    self.state = 18
                    self.simpleObj()
                    self.state = 23
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 24
                self.match(JSONTableParser.T__2)
                pass

            elif la_ == 2:
                localctx = JSONTableParser.ArrTableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(JSONTableParser.T__0)
                self.state = 27
                self.simpleArr()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 28
                    self.match(JSONTableParser.T__1)
                    self.state = 29
                    self.simpleArr()
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(JSONTableParser.T__2)
                pass

            elif la_ == 3:
                localctx = JSONTableParser.ArrTableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(JSONTableParser.T__0)
                self.state = 38
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
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(JSONTableParser.T__3)
                self.state = 42
                self.pair()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 43
                    self.match(JSONTableParser.T__1)
                    self.state = 44
                    self.pair()
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(JSONTableParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(JSONTableParser.T__3)
                self.state = 53
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
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(JSONTableParser.T__0)
                self.state = 57
                self.simpleValue()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONTableParser.T__1:
                    self.state = 58
                    self.match(JSONTableParser.T__1)
                    self.state = 59
                    self.simpleValue()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.match(JSONTableParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(JSONTableParser.T__0)
                self.state = 68
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
            self.state = 71
            self.match(JSONTableParser.STRING)
            self.state = 72
            self.match(JSONTableParser.T__5)
            self.state = 73
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
            self.state = 75
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





