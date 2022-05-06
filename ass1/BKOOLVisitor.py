# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attr.
    def visitAttr(self, ctx:BKOOLParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#meth.
    def visitMeth(self, ctx:BKOOLParser.MethContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstm.
    def visitBlockstm(self, ctx:BKOOLParser.BlockstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varclr.
    def visitVarclr(self, ctx:BKOOLParser.VarclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asmstm.
    def visitAsmstm(self, ctx:BKOOLParser.AsmstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifstm.
    def visitIfstm(self, ctx:BKOOLParser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forstm.
    def visitForstm(self, ctx:BKOOLParser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#brkstm.
    def visitBrkstm(self, ctx:BKOOLParser.BrkstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constm.
    def visitConstm(self, ctx:BKOOLParser.ConstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#rtstm.
    def visitRtstm(self, ctx:BKOOLParser.RtstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invstm.
    def visitInvstm(self, ctx:BKOOLParser.InvstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraylit.
    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#boollit.
    def visitBoollit(self, ctx:BKOOLParser.BoollitContext):
        return self.visitChildren(ctx)



del BKOOLParser