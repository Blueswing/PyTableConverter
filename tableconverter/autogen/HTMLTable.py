# Generated from HTMLTable.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\7\2\30\n\2\f\2\16\2\33")
        buf.write("\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2$\n\2\3\2\5\2\'\n")
        buf.write("\2\3\2\5\2*\n\2\3\3\3\3\3\3\7\3/\n\3\f\3\16\3\62\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\3\3\3\3\3")
        buf.write("\5\3A\n\3\3\4\5\4D\n\4\3\4\3\4\3\4\5\4I\n\4\3\4\5\4L\n")
        buf.write("\4\7\4N\n\4\f\4\16\4Q\13\4\3\5\3\5\3\5\5\5V\n\5\3\6\3")
        buf.write("\6\3\7\3\7\5\7\\\n\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\2\2\13\2\4\6\b\n\f\16\20\22\2\6\4\2\t\t\r\r\3\2\3\4")
        buf.write("\3\2\25\26\3\2\27\30\2l\2\24\3\2\2\2\4@\3\2\2\2\6C\3\2")
        buf.write("\2\2\bR\3\2\2\2\nW\3\2\2\2\f[\3\2\2\2\16]\3\2\2\2\20_")
        buf.write("\3\2\2\2\22b\3\2\2\2\24\25\7\f\2\2\25\31\7\16\2\2\26\30")
        buf.write("\5\b\5\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32&\3\2\2\2\33\31\3\2\2\2\34#\7\17\2\2\35")
        buf.write("\36\5\6\4\2\36\37\7\f\2\2\37 \7\21\2\2 !\7\16\2\2!\"\7")
        buf.write("\17\2\2\"$\3\2\2\2#\35\3\2\2\2#$\3\2\2\2$\'\3\2\2\2%\'")
        buf.write("\7\20\2\2&\34\3\2\2\2&%\3\2\2\2\')\3\2\2\2(*\7\2\2\3)")
        buf.write("(\3\2\2\2)*\3\2\2\2*\3\3\2\2\2+,\7\f\2\2,\60\7\23\2\2")
        buf.write("-/\5\b\5\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61;\3\2\2\2\62\60\3\2\2\2\63\64\7\17\2\2\64\65\5")
        buf.write("\6\4\2\65\66\7\f\2\2\66\67\7\21\2\2\678\7\23\2\289\7\17")
        buf.write("\2\29<\3\2\2\2:<\7\20\2\2;\63\3\2\2\2;:\3\2\2\2<A\3\2")
        buf.write("\2\2=A\7\b\2\2>A\5\20\t\2?A\5\22\n\2@+\3\2\2\2@=\3\2\2")
        buf.write("\2@>\3\2\2\2@?\3\2\2\2A\5\3\2\2\2BD\5\n\6\2CB\3\2\2\2")
        buf.write("CD\3\2\2\2DO\3\2\2\2EI\5\4\3\2FI\7\6\2\2GI\5\16\b\2HE")
        buf.write("\3\2\2\2HF\3\2\2\2HG\3\2\2\2IK\3\2\2\2JL\5\n\6\2KJ\3\2")
        buf.write("\2\2KL\3\2\2\2LN\3\2\2\2MH\3\2\2\2NQ\3\2\2\2OM\3\2\2\2")
        buf.write("OP\3\2\2\2P\7\3\2\2\2QO\3\2\2\2RU\7\23\2\2ST\7\22\2\2")
        buf.write("TV\7\31\2\2US\3\2\2\2UV\3\2\2\2V\t\3\2\2\2WX\t\2\2\2X")
        buf.write("\13\3\2\2\2Y\\\5\16\b\2Z\\\7\t\2\2[Y\3\2\2\2[Z\3\2\2\2")
        buf.write("\\\r\3\2\2\2]^\t\3\2\2^\17\3\2\2\2_`\7\n\2\2`a\t\4\2\2")
        buf.write("a\21\3\2\2\2bc\7\13\2\2cd\t\5\2\2d\23\3\2\2\2\17\31#&")
        buf.write(")\60;@CHKOU[")
        return buf.getvalue()


class HTMLTable ( Parser ):

    grammarFileName = "HTMLTable.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<'", "<INVALID>", "'table'", 
                     "'>'", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "HTML_COMMENT", "HTML_CONDITIONAL_COMMENT", 
                      "XML", "CDATA", "DTD", "SCRIPTLET", "SEA_WS", "SCRIPT_OPEN", 
                      "STYLE_OPEN", "TAG_OPEN", "HTML_TEXT", "TAG_TABLE", 
                      "TAG_CLOSE", "TAG_SLASH_CLOSE", "TAG_SLASH", "TAG_EQUALS", 
                      "TAG_NAME", "TAG_WHITESPACE", "SCRIPT_BODY", "SCRIPT_SHORT_BODY", 
                      "STYLE_BODY", "STYLE_SHORT_BODY", "ATTVALUE_VALUE", 
                      "ATTRIBUTE" ]

    RULE_table = 0
    RULE_htmlElement = 1
    RULE_htmlContent = 2
    RULE_htmlAttribute = 3
    RULE_htmlChardata = 4
    RULE_htmlMisc = 5
    RULE_htmlComment = 6
    RULE_script = 7
    RULE_style = 8

    ruleNames =  [ "table", "htmlElement", "htmlContent", "htmlAttribute", 
                   "htmlChardata", "htmlMisc", "htmlComment", "script", 
                   "style" ]

    EOF = Token.EOF
    HTML_COMMENT=1
    HTML_CONDITIONAL_COMMENT=2
    XML=3
    CDATA=4
    DTD=5
    SCRIPTLET=6
    SEA_WS=7
    SCRIPT_OPEN=8
    STYLE_OPEN=9
    TAG_OPEN=10
    HTML_TEXT=11
    TAG_TABLE=12
    TAG_CLOSE=13
    TAG_SLASH_CLOSE=14
    TAG_SLASH=15
    TAG_EQUALS=16
    TAG_NAME=17
    TAG_WHITESPACE=18
    SCRIPT_BODY=19
    SCRIPT_SHORT_BODY=20
    STYLE_BODY=21
    STYLE_SHORT_BODY=22
    ATTVALUE_VALUE=23
    ATTRIBUTE=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLTable.TAG_OPEN)
            else:
                return self.getToken(HTMLTable.TAG_OPEN, i)

        def TAG_TABLE(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLTable.TAG_TABLE)
            else:
                return self.getToken(HTMLTable.TAG_TABLE, i)

        def TAG_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLTable.TAG_CLOSE)
            else:
                return self.getToken(HTMLTable.TAG_CLOSE, i)

        def TAG_SLASH_CLOSE(self):
            return self.getToken(HTMLTable.TAG_SLASH_CLOSE, 0)

        def htmlAttribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLTable.HtmlAttributeContext)
            else:
                return self.getTypedRuleContext(HTMLTable.HtmlAttributeContext,i)


        def EOF(self):
            return self.getToken(HTMLTable.EOF, 0)

        def htmlContent(self):
            return self.getTypedRuleContext(HTMLTable.HtmlContentContext,0)


        def TAG_SLASH(self):
            return self.getToken(HTMLTable.TAG_SLASH, 0)

        def getRuleIndex(self):
            return HTMLTable.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = HTMLTable.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(HTMLTable.TAG_OPEN)
            self.state = 19
            self.match(HTMLTable.TAG_TABLE)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HTMLTable.TAG_NAME:
                self.state = 20
                self.htmlAttribute()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HTMLTable.TAG_CLOSE]:
                self.state = 26
                self.match(HTMLTable.TAG_CLOSE)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HTMLTable.HTML_COMMENT) | (1 << HTMLTable.HTML_CONDITIONAL_COMMENT) | (1 << HTMLTable.CDATA) | (1 << HTMLTable.SCRIPTLET) | (1 << HTMLTable.SEA_WS) | (1 << HTMLTable.SCRIPT_OPEN) | (1 << HTMLTable.STYLE_OPEN) | (1 << HTMLTable.TAG_OPEN) | (1 << HTMLTable.HTML_TEXT))) != 0):
                    self.state = 27
                    self.htmlContent()
                    self.state = 28
                    self.match(HTMLTable.TAG_OPEN)
                    self.state = 29
                    self.match(HTMLTable.TAG_SLASH)
                    self.state = 30
                    self.match(HTMLTable.TAG_TABLE)
                    self.state = 31
                    self.match(HTMLTable.TAG_CLOSE)


                pass
            elif token in [HTMLTable.TAG_SLASH_CLOSE]:
                self.state = 35
                self.match(HTMLTable.TAG_SLASH_CLOSE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(HTMLTable.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HTMLTable.RULE_htmlElement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IgnoredContext(HtmlElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HTMLTable.HtmlElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCRIPTLET(self):
            return self.getToken(HTMLTable.SCRIPTLET, 0)
        def script(self):
            return self.getTypedRuleContext(HTMLTable.ScriptContext,0)

        def style(self):
            return self.getTypedRuleContext(HTMLTable.StyleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnored" ):
                listener.enterIgnored(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnored" ):
                listener.exitIgnored(self)


    class NormalTagContext(HtmlElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HTMLTable.HtmlElementContext
            super().__init__(parser)
            self.tag = None # Token
            self.content = None # HtmlContentContext
            self.copyFrom(ctx)

        def TAG_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLTable.TAG_OPEN)
            else:
                return self.getToken(HTMLTable.TAG_OPEN, i)
        def TAG_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLTable.TAG_NAME)
            else:
                return self.getToken(HTMLTable.TAG_NAME, i)
        def TAG_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLTable.TAG_CLOSE)
            else:
                return self.getToken(HTMLTable.TAG_CLOSE, i)
        def TAG_SLASH(self):
            return self.getToken(HTMLTable.TAG_SLASH, 0)
        def TAG_SLASH_CLOSE(self):
            return self.getToken(HTMLTable.TAG_SLASH_CLOSE, 0)
        def htmlAttribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLTable.HtmlAttributeContext)
            else:
                return self.getTypedRuleContext(HTMLTable.HtmlAttributeContext,i)

        def htmlContent(self):
            return self.getTypedRuleContext(HTMLTable.HtmlContentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalTag" ):
                listener.enterNormalTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalTag" ):
                listener.exitNormalTag(self)



    def htmlElement(self):

        localctx = HTMLTable.HtmlElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_htmlElement)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HTMLTable.TAG_OPEN]:
                localctx = HTMLTable.NormalTagContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(HTMLTable.TAG_OPEN)
                self.state = 42
                localctx.tag = self.match(HTMLTable.TAG_NAME)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HTMLTable.TAG_NAME:
                    self.state = 43
                    self.htmlAttribute()
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [HTMLTable.TAG_CLOSE]:
                    self.state = 49
                    self.match(HTMLTable.TAG_CLOSE)
                    self.state = 50
                    localctx.content = self.htmlContent()
                    self.state = 51
                    self.match(HTMLTable.TAG_OPEN)
                    self.state = 52
                    self.match(HTMLTable.TAG_SLASH)
                    self.state = 53
                    self.match(HTMLTable.TAG_NAME)
                    self.state = 54
                    self.match(HTMLTable.TAG_CLOSE)
                    pass
                elif token in [HTMLTable.TAG_SLASH_CLOSE]:
                    self.state = 56
                    self.match(HTMLTable.TAG_SLASH_CLOSE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [HTMLTable.SCRIPTLET]:
                localctx = HTMLTable.IgnoredContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(HTMLTable.SCRIPTLET)
                pass
            elif token in [HTMLTable.SCRIPT_OPEN]:
                localctx = HTMLTable.IgnoredContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.script()
                pass
            elif token in [HTMLTable.STYLE_OPEN]:
                localctx = HTMLTable.IgnoredContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.style()
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


    class HtmlContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlChardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLTable.HtmlChardataContext)
            else:
                return self.getTypedRuleContext(HTMLTable.HtmlChardataContext,i)


        def htmlElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLTable.HtmlElementContext)
            else:
                return self.getTypedRuleContext(HTMLTable.HtmlElementContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLTable.CDATA)
            else:
                return self.getToken(HTMLTable.CDATA, i)

        def htmlComment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLTable.HtmlCommentContext)
            else:
                return self.getTypedRuleContext(HTMLTable.HtmlCommentContext,i)


        def getRuleIndex(self):
            return HTMLTable.RULE_htmlContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlContent" ):
                listener.enterHtmlContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlContent" ):
                listener.exitHtmlContent(self)




    def htmlContent(self):

        localctx = HTMLTable.HtmlContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_htmlContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HTMLTable.SEA_WS or _la==HTMLTable.HTML_TEXT:
                self.state = 64
                self.htmlChardata()


            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [HTMLTable.SCRIPTLET, HTMLTable.SCRIPT_OPEN, HTMLTable.STYLE_OPEN, HTMLTable.TAG_OPEN]:
                        self.state = 67
                        self.htmlElement()
                        pass
                    elif token in [HTMLTable.CDATA]:
                        self.state = 68
                        self.match(HTMLTable.CDATA)
                        pass
                    elif token in [HTMLTable.HTML_COMMENT, HTMLTable.HTML_CONDITIONAL_COMMENT]:
                        self.state = 69
                        self.htmlComment()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HTMLTable.SEA_WS or _la==HTMLTable.HTML_TEXT:
                        self.state = 72
                        self.htmlChardata()

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlAttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_NAME(self):
            return self.getToken(HTMLTable.TAG_NAME, 0)

        def TAG_EQUALS(self):
            return self.getToken(HTMLTable.TAG_EQUALS, 0)

        def ATTVALUE_VALUE(self):
            return self.getToken(HTMLTable.ATTVALUE_VALUE, 0)

        def getRuleIndex(self):
            return HTMLTable.RULE_htmlAttribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlAttribute" ):
                listener.enterHtmlAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlAttribute" ):
                listener.exitHtmlAttribute(self)




    def htmlAttribute(self):

        localctx = HTMLTable.HtmlAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_htmlAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(HTMLTable.TAG_NAME)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HTMLTable.TAG_EQUALS:
                self.state = 81
                self.match(HTMLTable.TAG_EQUALS)
                self.state = 82
                self.match(HTMLTable.ATTVALUE_VALUE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlChardataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HTML_TEXT(self):
            return self.getToken(HTMLTable.HTML_TEXT, 0)

        def SEA_WS(self):
            return self.getToken(HTMLTable.SEA_WS, 0)

        def getRuleIndex(self):
            return HTMLTable.RULE_htmlChardata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlChardata" ):
                listener.enterHtmlChardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlChardata" ):
                listener.exitHtmlChardata(self)




    def htmlChardata(self):

        localctx = HTMLTable.HtmlChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_htmlChardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==HTMLTable.SEA_WS or _la==HTMLTable.HTML_TEXT):
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


    class HtmlMiscContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlComment(self):
            return self.getTypedRuleContext(HTMLTable.HtmlCommentContext,0)


        def SEA_WS(self):
            return self.getToken(HTMLTable.SEA_WS, 0)

        def getRuleIndex(self):
            return HTMLTable.RULE_htmlMisc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlMisc" ):
                listener.enterHtmlMisc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlMisc" ):
                listener.exitHtmlMisc(self)




    def htmlMisc(self):

        localctx = HTMLTable.HtmlMiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_htmlMisc)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HTMLTable.HTML_COMMENT, HTMLTable.HTML_CONDITIONAL_COMMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.htmlComment()
                pass
            elif token in [HTMLTable.SEA_WS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(HTMLTable.SEA_WS)
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


    class HtmlCommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HTML_COMMENT(self):
            return self.getToken(HTMLTable.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLTable.HTML_CONDITIONAL_COMMENT, 0)

        def getRuleIndex(self):
            return HTMLTable.RULE_htmlComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlComment" ):
                listener.enterHtmlComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlComment" ):
                listener.exitHtmlComment(self)




    def htmlComment(self):

        localctx = HTMLTable.HtmlCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_htmlComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==HTMLTable.HTML_COMMENT or _la==HTMLTable.HTML_CONDITIONAL_COMMENT):
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


    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLTable.SCRIPT_OPEN, 0)

        def SCRIPT_BODY(self):
            return self.getToken(HTMLTable.SCRIPT_BODY, 0)

        def SCRIPT_SHORT_BODY(self):
            return self.getToken(HTMLTable.SCRIPT_SHORT_BODY, 0)

        def getRuleIndex(self):
            return HTMLTable.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = HTMLTable.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(HTMLTable.SCRIPT_OPEN)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==HTMLTable.SCRIPT_BODY or _la==HTMLTable.SCRIPT_SHORT_BODY):
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


    class StyleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STYLE_OPEN(self):
            return self.getToken(HTMLTable.STYLE_OPEN, 0)

        def STYLE_BODY(self):
            return self.getToken(HTMLTable.STYLE_BODY, 0)

        def STYLE_SHORT_BODY(self):
            return self.getToken(HTMLTable.STYLE_SHORT_BODY, 0)

        def getRuleIndex(self):
            return HTMLTable.RULE_style

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyle" ):
                listener.enterStyle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyle" ):
                listener.exitStyle(self)




    def style(self):

        localctx = HTMLTable.StyleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_style)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(HTMLTable.STYLE_OPEN)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==HTMLTable.STYLE_BODY or _la==HTMLTable.STYLE_SHORT_BODY):
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





