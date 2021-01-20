# Generated from JSONTable.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONTableParser import JSONTableParser
else:
    from JSONTableParser import JSONTableParser

# This class defines a complete listener for a parse tree produced by JSONTableParser.
class JSONTableListener(ParseTreeListener):

    # Enter a parse tree produced by JSONTableParser#table.
    def enterTable(self, ctx:JSONTableParser.TableContext):
        pass

    # Exit a parse tree produced by JSONTableParser#table.
    def exitTable(self, ctx:JSONTableParser.TableContext):
        pass


    # Enter a parse tree produced by JSONTableParser#objTable.
    def enterObjTable(self, ctx:JSONTableParser.ObjTableContext):
        pass

    # Exit a parse tree produced by JSONTableParser#objTable.
    def exitObjTable(self, ctx:JSONTableParser.ObjTableContext):
        pass


    # Enter a parse tree produced by JSONTableParser#arrTable.
    def enterArrTable(self, ctx:JSONTableParser.ArrTableContext):
        pass

    # Exit a parse tree produced by JSONTableParser#arrTable.
    def exitArrTable(self, ctx:JSONTableParser.ArrTableContext):
        pass


    # Enter a parse tree produced by JSONTableParser#simpleObj.
    def enterSimpleObj(self, ctx:JSONTableParser.SimpleObjContext):
        pass

    # Exit a parse tree produced by JSONTableParser#simpleObj.
    def exitSimpleObj(self, ctx:JSONTableParser.SimpleObjContext):
        pass


    # Enter a parse tree produced by JSONTableParser#simpleArr.
    def enterSimpleArr(self, ctx:JSONTableParser.SimpleArrContext):
        pass

    # Exit a parse tree produced by JSONTableParser#simpleArr.
    def exitSimpleArr(self, ctx:JSONTableParser.SimpleArrContext):
        pass


    # Enter a parse tree produced by JSONTableParser#pair.
    def enterPair(self, ctx:JSONTableParser.PairContext):
        pass

    # Exit a parse tree produced by JSONTableParser#pair.
    def exitPair(self, ctx:JSONTableParser.PairContext):
        pass


    # Enter a parse tree produced by JSONTableParser#simpleValue.
    def enterSimpleValue(self, ctx:JSONTableParser.SimpleValueContext):
        pass

    # Exit a parse tree produced by JSONTableParser#simpleValue.
    def exitSimpleValue(self, ctx:JSONTableParser.SimpleValueContext):
        pass



del JSONTableParser