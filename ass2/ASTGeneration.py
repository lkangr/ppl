#from main.bkool.utils.AST import ArrayCell, ArrayLiteral, ArrayType, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, CallStmt, ClassDecl, ClassType, ConstDecl, Continue, FieldAccess, FloatLiteral, FloatType, For, Id, If, Instance, IntLiteral, IntType, MethodDecl, NewExpr, NullLiteral, Program, Return, SelfLiteral, Static, StringLiteral, StringType, UnaryOp, VarDecl, VoidType
from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):  
        mem = reduce(lambda a, b: a + self.visit(b), ctx.memdecl(), [])
        if ctx.ID(1) == None:
            return ClassDecl(Id(ctx.ID(0).getText()), mem)
        return ClassDecl(Id(ctx.ID(0).getText()), mem, Id(ctx.ID(1).getText()))

    def visitMemdecl(self, ctx:BKOOLParser.MemdeclContext):
        if ctx.attributedecl() != None:
           return self.visit(ctx.attributedecl())
        return self.visit(ctx.methoddecl())

    def visitAttributedecl(self, ctx:BKOOLParser.AttributedeclContext):
        kind = Instance()
        if ctx.STATIC() != None: kind = Static()
        if ctx.FINAL() != None:
            return reduce(lambda a, b: a + [AttributeDecl(kind, ConstDecl(self.visit(ctx.varatt(b))[0], self.visit(ctx.typ()), self.visit(ctx.varatt(b))[1]))], range(len(ctx.varatt())), [])
        return reduce(lambda a, b: a + [AttributeDecl(kind, VarDecl(self.visit(ctx.varatt(b))[0], self.visit(ctx.typ()), self.visit(ctx.varatt(b))[1]))], range(len(ctx.varatt())), [])

    def visitVaratt(self, ctx:BKOOLParser.VarattContext):
        a = None
        if ctx.expr() != None:
            a = self.visit(ctx.expr())
        return [Id(ctx.ID().getText()), a]

    def visitMethoddecl(self, ctx:BKOOLParser.MethoddeclContext):
        kind = Instance()
        if ctx.STATIC() != None: kind = Static()
        tp = None
        name = Id(ctx.ID().getText())
        if ctx.typ() != None: 
            tp = self.visit(ctx.typ())
            if ctx.ID().getText() == "main": kind = Static()
        else: name = Id("<init>")
        param = reduce(lambda a, b: a + self.visit(b), ctx.varmet(), [])
        return [MethodDecl(kind, name, param, tp, self.visit(ctx.block()))]

    def visitVarmet(self, ctx:BKOOLParser.VarmetContext):
        return reduce(lambda a, b: a + [VarDecl(Id(b.getText()), self.visit(ctx.typ()))], ctx.ID(), [])

    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1())
        if ctx.LT() != None: cp = ctx.LT().getText()
        elif ctx.GT() != None: cp = ctx.GT().getText()
        elif ctx.LTE() != None: cp = ctx.LTE().getText()
        else: cp = ctx.GTE().getText()
        return BinaryOp(cp, self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2())
        if ctx.EQ() != None: cp = ctx.EQ().getText()
        else: cp = ctx.NEQ().getText()
        return BinaryOp(cp, self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))

    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        if ctx.LAND() != None: cp = ctx.LAND().getText()
        else: cp = ctx.LOR().getText()
        return BinaryOp(cp, self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        if ctx.ADDOP() != None: cp = ctx.ADDOP().getText()
        else: cp = ctx.SUBOP().getText()
        return BinaryOp(cp, self.visit(ctx.expr3()), self.visit(ctx.expr4()))

    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        if ctx.MULOP() != None: cp = ctx.MULOP().getText()
        elif ctx.IDIVOP() != None: cp = ctx.IDIVOP().getText()
        elif ctx.FDIVOP() != None: cp = ctx.FDIVOP().getText()
        else: cp = ctx.MODOP().getText()
        return BinaryOp(cp, self.visit(ctx.expr4()), self.visit(ctx.expr5()))

    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        return BinaryOp(ctx.CON().getText(), self.visit(ctx.expr5()), self.visit(ctx.expr6()))

    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnaryOp(ctx.LNOT().getText(), self.visit(ctx.expr6()))

    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        if ctx.ADDOP() != None: cp = ctx.ADDOP().getText()
        else: cp = ctx.SUBOP().getText()
        return UnaryOp(cp, self.visit(ctx.expr7()))

    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        return ArrayCell(self.visit(ctx.expr9()), self.visit(ctx.expr()))

    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        if ctx.LB() == None:
            return FieldAccess(self.visit(ctx.expr9()), Id(ctx.ID().getText()))
        param = reduce(lambda a, b: a + [self.visit(b)], ctx.expr(), [])
        return CallExpr(self.visit(ctx.expr9()), Id(ctx.ID().getText()), param)

    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr11())
        param = reduce(lambda a, b: a + [self.visit(b)], ctx.expr(), [])
        return NewExpr(Id(ctx.ID().getText()), param)

    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        if ctx.literal() != None:
            return self.visit(ctx.literal())
        return Id(ctx.ID().getText())

    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        if ctx.INTLIT() != None: return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT() != None: return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.boollit() != None: return self.visit(ctx.boollit())
        if ctx.STRINGLIT() != None: return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.arraylit() != None: return self.visit(ctx.arraylit())
        if ctx.NILLIT() != None: return NullLiteral()
        return SelfLiteral()

    def visitBoollit(self, ctx:BKOOLParser.BoollitContext):
        if ctx.BTRUE() != None: return BooleanLiteral(True)
        return BooleanLiteral(False)

    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return ArrayLiteral(reduce(lambda a, b: a + [self.visit(ctx.alit(b))], range(len(ctx.alit())), []))    

    def visitAlit(self, ctx:BKOOLParser.AlitContext):
        if ctx.INTLIT() != None: return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT() != None: return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.boollit() != None: return self.visit(ctx.boollit())
        if ctx.STRINGLIT() != None: return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.NILLIT() != None: return NullLiteral()
        return SelfLiteral()

    def visitBlock(self, ctx:BKOOLParser.BlockContext):
        decl = reduce(lambda a, b: a + self.visit(b), ctx.vardecl(), [])
        stmt = [self.visit(x) for x in ctx.stmt()]
        return Block(decl, stmt)

    def visitVardecl(self, ctx:BKOOLParser.VardeclContext): 
        if ctx.FINAL() != None:
            return reduce(lambda a, b: a + [ConstDecl(self.visit(ctx.varatt(b))[0], self.visit(ctx.typ()), self.visit(ctx.varatt(b))[1])], range(len(ctx.varatt())), [])
        return reduce(lambda a, b: a + [VarDecl(self.visit(ctx.varatt(b))[0], self.visit(ctx.typ()), self.visit(ctx.varatt(b))[1])], range(len(ctx.varatt())), [])

    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitAsmstm(self, ctx:BKOOLParser.AsmstmContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        if ctx.getChildCount() == 1: return Id(ctx.ID().getText())
        if ctx.getChildCount() == 3: return FieldAccess(self.visit(ctx.expr9()), Id(ctx.ID().getText()))
        return ArrayCell(self.visit(ctx.expr9()), self.visit(ctx.expr()))

    def visitIfstm(self, ctx:BKOOLParser.IfstmContext):
        elstm = None
        if ctx.ELSE() != None: elstm = self.visit(ctx.stmt(1))
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), elstm)

    def visitForstm(self, ctx:BKOOLParser.ForstmContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), True if ctx.TO() != None else False, self.visit(ctx.stmt()))

    def visitBrkstm(self, ctx:BKOOLParser.BrkstmContext):
        return Break()

    def visitConstm(self, ctx:BKOOLParser.ConstmContext):
        return Continue()

    def visitRtstm(self, ctx:BKOOLParser.RtstmContext):
        return Return(self.visit(ctx.expr()))

    def visitInvstm(self, ctx:BKOOLParser.InvstmContext):
        param = reduce(lambda a, b: a + [self.visit(b)], ctx.expr()[1:], [])
        return CallStmt(self.visit(ctx.expr(0)), Id(ctx.ID().getText()), param)

    def visitTyp(self, ctx:BKOOLParser.TypContext):
        if ctx.INTTYPE() != None: return IntType()
        if ctx.FLOATTYPE() != None: return FloatType()
        if ctx.BOOLTYPE() != None: return BoolType()
        if ctx.STRINGTYPE() != None: return StringType()
        if ctx.VOIDTYPE() != None: return VoidType()
        if ctx.arraytype() != None: return self.visit(ctx.arraytype())
        return ClassType(Id(ctx.ID().getText()))

    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        if ctx.INTTYPE() != None: tp = IntType()
        elif ctx.FLOATTYPE() != None: tp = FloatType()
        elif ctx.BOOLTYPE() != None: tp = BoolType()
        elif ctx.STRINGTYPE() != None: tp = StringType()
        else: tp =  ClassType(Id(ctx.ID().getText()))
        return ArrayType(int(ctx.INTLIT().getText()), tp)