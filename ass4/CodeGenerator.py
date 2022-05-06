from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import * 
from AST import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"

from Emitter import Emitter

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("writeInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("writeIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("writeFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
                Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("writeBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("readStr", MType(list(), StringType()), CName(self.libName)),
                Symbol("writeStr", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("writeStrLn", MType([StringType()], VoidType()), CName(self.libName))
            ]

    def gen(self, ast,path):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl,path)
        gc.visit(ast, None)

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env,path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i,c) for i in ast.decl]
        return c

    def visitClassDecl(self,ast,c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object" if not ast.parentname else ast.parentname.name))

        ini = [self.visit(ele, SubBody(None, self.env)) for ele in ast.memlist if type(ele) == AttributeDecl]

        self.env = [self.visit(ele, SubBody(ini, self.env)) for ele in ast.memlist if type(ele) == MethodDecl] + self.env
        # generate default constructor
        if next(filter(lambda x: "<init>" == x.name,self.env),None) == None:
            self.genMETHOD(MethodDecl(Instance(),Id("<init>"), list(), None,Block([],[])), SubBody(Frame("<init>", VoidType()),self.env), ini)
        self.emit.emitEPILOG()
        return c

    def visitAttributeDecl(self,ast,o):
        o.sym = type(ast.kind)
        return self.visit(ast.decl, o)

    def visitVarDecl(self,ast,o):
        name = ast.variable.name
        typ = ast.varType
        kind = None
        if o.sym == Static or o.sym == Instance: kind = o.sym
        if kind:
            self.emit.printout(self.emit.emitATTRIBUTE(name, typ, False))
            self.env = [Symbol(name, typ, CName(self.className))] + self.env
            if ast.varInit:
                return lambda x: self.visit(ast.varInit, Access(x, self.env, False, False))[0] + self.emit.emitPUTSTATIC(self.className+'.'+name, typ,x)
            else: 
                return lambda x: ""
        else:
            index = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, name, typ, o.frame.getStartLabel(), o.frame.getEndLabel(),o.frame))
            o.sym = [Symbol(name, typ, Index(index))] + o.sym
            if ast.varInit:
                return self.visit(ast.varInit, Access(o.frame, o.sym, False, False))[0] + self.emit.emitWRITEVAR(name, typ, index, o.frame)
            else:
                return ""

    
    def visitConstDecl(self,ast,o):
        name = ast.constant.name
        typ = ast.constType
        kind = None
        if o.sym == Static or o.sym == Instance: kind = o.sym
        if kind:
            self.emit.printout(self.emit.emitATTRIBUTE(name, typ, False))
            self.env = [Symbol(name, typ, CName(self.className))] + self.env
            if ast.value:
                return lambda x: self.visit(ast.value, Access(x, self.env, False, False))[0] + self.emit.emitPUTSTATIC(self.className+'.'+name, typ,x)
            else: 
                return lambda x: ""
        else:
            index = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, name, typ, o.frame.getStartLabel(), o.frame.getEndLabel(),o.frame))
            o.sym = [Symbol(name, typ, Index(index))] + o.sym
            if ast.value:
                return self.visit(ast.value, Access(o.frame, o.sym, False, False))[0] + self.emit.emitWRITEVAR(name, typ, index, o.frame)
            else:
                return ""

    def genMETHOD(self, consdecl, o, ini = list()):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0,StringType())] if isMain else list(map(lambda x: x.varType,consdecl.param))
        mtype = MType(intype, returnType)
        isStatic = type(consdecl.kind) == Static

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, o.frame))

        o.frame.enterScope(True)

        # Generate code for parameter declarations
        ind = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(ind, "this", ClassType(Id(self.className)), o.frame.getStartLabel(), o.frame.getEndLabel(),o.frame))
        o.sym = [Symbol("this", ClassType(Id(self.className)),Index(ind))] + o.sym
        linit = ''

        if isMain:
            ind_ = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(ind_, "args", ArrayType(0,StringType()), o.frame.getStartLabel(), o.frame.getEndLabel(),o.frame))
            o.sym = [Symbol("args", ArrayType(0,StringType()),Index(ind_))] + o.sym
        else:
            linit = ''.join([self.visit(x,o) for x in consdecl.param])
        
        body = consdecl.body
        linit += ''.join([self.visit(x,o) for x in body.decl])
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, o.frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(o.frame))
            self.emit.printout("".join(list(map(lambda x: x(o.frame), ini))))
        elif isMain:
            self.emit.printout("".join(list(map(lambda x: x(o.frame), ini))))
  
        self.emit.printout(linit)
        list(map(lambda x: self.visit(x, o), body.stmt))

        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))
        self.emit.printout(self.emit.emitENDMETHOD(o.frame))
        o.frame.exitScope();

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name.name, ast.returnType)
        self.genMETHOD(ast, SubBody(frame,o.sym), o.frame)
        return Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))

    def visitIntLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(ast.value,o.frame),IntType()
    
    def visitFloatLiteral(self,ast,o):
        return self.emit.emitPUSHFCONST(ast.value,o.frame),FloatType()
    
    def visitStringLiteral(self,ast,o):
        return self.emit.emitPUSHCONST(ast.value,StringType(),o.frame),StringType()
    
    def visitBooleanLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(str(ast.value),o.frame),BoolType()
        
    def visitArrayLiteral(self,ast,o):
        size = len(ast.value)
        if type(ast.value[0]) is IntLiteral: typ = IntType()
        elif type(ast.value[0]) is FloatLiteral: typ = FloatType()
        elif type(ast.value[0]) is StringLiteral: typ = StringType()
        elif type(ast.value[0]) is BooleanLiteral: typ = BoolType()
        buffer = list()
        buffer.append(self.emit.emitNEWARRAY(size,typ,o.frame))
        for ind in range(size):
            buffer.append(self.emit.emitDUP(o.frame))
            buffer.append(self.emit.emitPUSHICONST(ind, o.frame))
            buffer.append(self.visit(ast.value[ind],o)[0])
            buffer.append(self.emit.emitASTORE(typ, o.frame))
        return ''.join(buffer), ArrayType(size, typ)
    
    def visitSelfLiteral(self,ast,o):
        return self.emit.emitREADVAR('this', ClassType(Id(self.className)), 0, o.frame), ClassType(Id(self.className))

    def visitBinaryOp(self, ast, o):
        rs = list()
        e1c,e1t = self.visit(ast.left,o)
        rs.append(e1c)
        e2c,e2t = self.visit(ast.right,o)
        typ = e1t
        if (type(e1t) is IntType) and ((type(e2t) is FloatType) or (ast.op == '/')):
            rs.append(self.emit.emitI2F(o.frame))
            typ = FloatType()
        rs.append(e2c)
        if (type(e2t) is IntType) and (type(typ) is FloatType):
           rs.append(self.emit.emitI2F(o.frame))
        if ast.op == '+' or ast.op == '-':
            rs.append(self.emit.emitADDOP(ast.op, typ, o.frame))
        elif ast.op == '*' or ast.op == '/':
            rs.append(self.emit.emitMULOP(ast.op, typ, o.frame))
        elif ast.op == '%':
            rs.append(self.emit.emitDIV(o.frame))
        elif ast.op == '\\':
            rs.append(self.emit.emitMOD(o.frame))
        elif ast.op == '&&':
            rs.append(self.emit.emitANDOP(o.frame))
        elif ast.op == '||':
            rs.append(self.emit.emitOROP(o.frame))
        else:
            rs.append(self.emit.emitREOP(ast.op,typ,o.frame))
        return ''.join(rs), typ
    
    def visitUnaryOp(self,ast,o):
        ec, et = self.visit(ast.body, o)
        if ast.op == '!':
            return ec + self.emit.emitNOT(et), et
        else:
            return self.visit(BinaryOp(ast.op,IntLiteral(0),ast.body), o)
    
    def visitCallExpr(self,ast,o):
        param = ''.join([self.visit(x, o)[0] for x in ast.param])
        id = self.visit(ast.method, Access(o.frame, o.sym, False, True))[0].replace('.','/')
        return param+id
    
    def visitNewExpr(self,ast,o):
        new = self.emit.emitNEW(ast.classname.name, o.frame)
        new += self.emit.emitDUP(o.frame)
        new += ''.join([self.visit(x, o)[0] for x in ast.param])
        init = next(filter(lambda x: "<init>" == x.name and ast.classname.name == x.value.value,self.env),None)
        new += self.emit.emitINVOKESPECIAL(o.frame, init.value.value+'/<init>', init.mtype)
        return new
    
    def visitId(self,ast,o):
        sm = next(filter(lambda x: ast.name == x.name,o.sym),None)
        if o.isLeft:
            if o.isFirst:
                return '', sm.mtype
            else:
                return self.emit.emitWRITEVAR(ast.name, sm.mtype, sm.value.value, o.frame), sm.mtype
        else:
            if o.isFirst:
                tm = next(filter(lambda x: ast.name == x.name and type(x.value) is CName,o.sym),None)
                return tm.value.value+'.'+tm.name, tm.mtype
            else:
                if sm:
                    return self.emit.emitREADVAR(ast.name, sm.mtype, sm.value.value, o.frame), sm.mtype
                else:
                    return '', None
    
    def visitArrayCell(self,ast,o):
        arrc, arrt = self.visit(ast.arr, Access(o.frame, o.sym, False, False))
        idxc, idct = self.visit(ast.idx, Access(o.frame, o.sym, False, False))
        if o.isLeft:
            if o.isFirst:
                return arrc + idxc, arrt.eleType
            else:
                return self.emit.emitASTORE(arrt.eleType, o.frame), arrt.eleType
        else:
            return arrc + idxc + self.emit.emitALOAD(arrt.eleType, o.frame), arrt.eleType
    
    def visitFieldAccess(self,ast,o):
        fnc, fnt = self.visit(ast.fieldname, Access(o.frame, o.sym, False, True))
        if o.isLeft:
            if o.isFirst:
                return '', fnt
            else:
                return self.emit.emitPUTSTATIC(fnc, fnt, o.frame), fnt
        else:
            return self.emit.emitGETSTATIC(fnc, fnt, o.frame), fnt
    
    def visitAssign(self,ast,o):
        rs = list()
        lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True, True))
        rs.append(lc)
        ec, et = self.visit(ast.exp, Access(o.frame, o.sym, False, False))
        rs.append(ec)
        if type(lt) is FloatType and type(et) is IntType:
            rs.append(self.emit.emitI2F(o.frame))
        lc2, lt2 = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
        rs.append(lc2)
        self.emit.printout(''.join(rs))
    
    def visitIf(self,ast,o):
        ec, et = self.visit(ast.expr, Access(o.frame, o.sym, False, False))
        labelT = o.frame.getNewLabel()
        labelE = o.frame.getNewLabel()
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitIFTRUE(labelT,o.frame))
        if ast.elseStmt: self.visit(ast.elseStmt,o)
        self.emit.printout(self.emit.emitGOTO(labelE,o.frame))
        self.emit.printout(self.emit.emitLABEL(labelT,o.frame))
        self.visit(ast.thenStmt,o)
        self.emit.printout(self.emit.emitLABEL(labelE,o.frame))
    
    def visitFor(self,ast,o):
        self.visit(Assign(ast.id, ast.expr1), o)
        self.emit.printout(self.visit(BinaryOp('-' if ast.up else '+', ast.id, IntLiteral(1)), Access(o.frame,o.sym,False,False))[0])
        o.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame))
        self.emit.printout(self.visit(BinaryOp('+' if ast.up else '-', ast.id, IntLiteral(1)), Access(o.frame,o.sym,False,False))[0])
        self.emit.printout(self.visit(BinaryOp('<=' if ast.up else '>=', ast.id, ast.expr2),Access(o.frame,o.sym,False,False))[0])
        self.emit.printout(self.emit.emitIFFALSE(o.frame.getBreakLabel(),o.frame))
        self.visit(ast.loop,o)
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(),o.frame))
        o.frame.exitLoop()
    
    def visitContinue(self,ast,o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame))
    
    def visitBreak(self,ast,o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(),o.frame))
    
    def visitReturn(self,ast,o):
        ec, et = self.visit(ast.expr, Access(o.frame,o.sym,False,False))
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitRETURN(et, o.frame))

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name,nenv),None)
        cname = sym.value.value    
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, False))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))




    
    def visitStatic(self,ast,param):
        return None
    
    def visitInstance(self,ast,param):
        return None
    
    def visitIntType(self,ast,param):
        return None
    
    def visitFloatType(self,ast,param):
        return None
    
    def visitBoolType(self,ast,param):
        return None
    
    def visitStringType(self,ast,param):
        return None
    
    def visitVoidType(self,ast,param):
        return None
    
    def visitArrayType(self,ast,param):
        return None
    
    def visitClassType(self,ast,param):
        return None
    
    def visitBlock(self,ast,param):
        return None
    
    def visitNullLiteral(self,ast,param):
        return None