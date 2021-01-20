# Generated from MarkdownTable.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MarkdownTableParser import MarkdownTableParser
else:
    from MarkdownTableParser import MarkdownTableParser

# This class defines a complete listener for a parse tree produced by MarkdownTableParser.
class MarkdownTableListener(ParseTreeListener):

    # Enter a parse tree produced by MarkdownTableParser#table.
    def enterTable(self, ctx:MarkdownTableParser.TableContext):
        pass

    # Exit a parse tree produced by MarkdownTableParser#table.
    def exitTable(self, ctx:MarkdownTableParser.TableContext):
        pass


    # Enter a parse tree produced by MarkdownTableParser#header.
    def enterHeader(self, ctx:MarkdownTableParser.HeaderContext):
        pass

    # Exit a parse tree produced by MarkdownTableParser#header.
    def exitHeader(self, ctx:MarkdownTableParser.HeaderContext):
        pass


    # Enter a parse tree produced by MarkdownTableParser#sepLine.
    def enterSepLine(self, ctx:MarkdownTableParser.SepLineContext):
        pass

    # Exit a parse tree produced by MarkdownTableParser#sepLine.
    def exitSepLine(self, ctx:MarkdownTableParser.SepLineContext):
        pass


    # Enter a parse tree produced by MarkdownTableParser#body.
    def enterBody(self, ctx:MarkdownTableParser.BodyContext):
        pass

    # Exit a parse tree produced by MarkdownTableParser#body.
    def exitBody(self, ctx:MarkdownTableParser.BodyContext):
        pass


    # Enter a parse tree produced by MarkdownTableParser#row.
    def enterRow(self, ctx:MarkdownTableParser.RowContext):
        pass

    # Exit a parse tree produced by MarkdownTableParser#row.
    def exitRow(self, ctx:MarkdownTableParser.RowContext):
        pass


    # Enter a parse tree produced by MarkdownTableParser#item.
    def enterItem(self, ctx:MarkdownTableParser.ItemContext):
        pass

    # Exit a parse tree produced by MarkdownTableParser#item.
    def exitItem(self, ctx:MarkdownTableParser.ItemContext):
        pass



del MarkdownTableParser