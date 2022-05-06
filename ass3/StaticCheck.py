
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
#from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class GlobalEnv(Visitor):
    def visitProgram(self, ast, c):
        c = {
            'io': {
                'parent': None,
                'mem': {
                    'readInt': {
                        'kind': 'static',
                        'returnType': 'int',
                        'param': {},
                        'body': {}
                    },
                    'writeInt': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'int'
                            }
                        },
                        'body': {}
                    },
                    'writeIntLn': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'int'
                            }
                        },
                        'body': {}
                    },
                    'readFloat': {
                        'kind': 'static',
                        'returnType': 'float',
                        'param': {},
                        'body': {}
                    },
                    'writeFloat': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'float'
                            }
                        },
                        'body': {}
                    },
                    'writeFloatLn': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'float'
                            }
                        },
                        'body': {}
                    },
                    'readBool': {
                        'kind': 'static',
                        'returnType': 'boolean',
                        'param': {},
                        'body': {}
                    },
                    'writeBool': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'boolean'
                            }
                        },
                        'body': {}
                    },
                    'writeBoolLn': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'boolean'
                            }
                        },
                        'body': {}
                    },
                    'readStr': {
                        'kind': 'static',
                        'returnType': 'string',
                        'param': {},
                        'body': {}
                    },
                    'writeStr': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'string'
                            }
                        },
                        'body': {}
                    },
                    'writeStrLn': {
                        'kind': 'static',
                        'returnType': 'void',
                        'param': {
                            'a': {
                                'isfinal': False,
                                'type': 'string'
                            }
                        },
                        'body': {}
                    },
                }
            }
        }
        return reduce(lambda b, x: b.update(self.visit(x,b)) or b, ast.decl, c)
    
    def visitClassDecl(self, ast, c):
        name = self.visit(ast.classname,{})
        if name in c.keys(): raise Redeclared(Class(),name)
        return {
            name: {
                'parent': self.visit(ast.parentname, {}) if ast.parentname else None, 
                'mem': reduce(lambda b, x: b.update(self.visit(x,b)) or b, ast.memlist, {})
                }
            }
    
    def visitAttributeDecl(self, ast, c):
        b = self.visit(ast.decl,{})
        if b[0] in c.keys(): raise Redeclared(Attribute(),b[0])
        b[1].update({'kind': self.visit(ast.kind,{})})
        return {b[0]: b[1]}
    
    def visitVarDecl(self, ast, c):
        name = self.visit(ast.variable,{})
        if name in c: raise Redeclared(Variable(),name)
        return [name, {
                'isfinal': False,
                'type': self.visit(ast.varType,{})
            }]
    
    def visitConstDecl(self, ast, c):
        name = self.visit(ast.constant,{})
        if name in c: raise Redeclared(Constant(),name)
        return [name, {
                'isfinal': True,
                'type': self.visit(ast.constType,{})
            }]
    
    def visitMethodDecl(self, ast, c):
        name = self.visit(ast.name,{})
        if name in c.keys(): raise Redeclared(Method(),name)

        def funcparam(b,m):
            if m[0] in b.keys():  raise Redeclared(Parameter(),m[0])
            b.update({m[0]: m[1]})
            return b

        param = reduce(lambda b, x: funcparam(b,self.visit(x,{})), ast.param, {})
        return {
            name: {
                'kind': self.visit(ast.kind,{}),
                'returnType': self.visit(ast.returnType,{}),
                'param': param,
                'body': self.visit(ast.body, param)
            }
        }
    
    def visitBlock(self, ast, c):
        def funcblock(b, m):
            b.update({m[0]: m[1]})
            return b

        return reduce(lambda b, x: funcblock(b,self.visit(x,list(b) + list(c))), ast.decl, {})
    
    def visitStatic(self, ast, c):
        return 'static'
    
    def visitInstance(self, ast, c):
        return 'instance'
    
    def visitIntType(self, ast, c):
        return 'int'
    
    def visitFloatType(self, ast, c):
        return 'float'
    
    def visitBoolType(self, ast, c):
        return 'boolean'
    
    def visitStringType(self, ast, c):
        return 'string'
    
    def visitVoidType(self, ast, c):
        return 'void'
    
    def visitArrayType(self, ast, c):
        return {'eleType': self.visit(ast.eleType,c), 'size': ast.size}
    
    def visitClassType(self, ast, c):
        return self.visit(ast.classname,c)
    
    def visitId(self, ast, c):
        return ast.name
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitNewExpr(self, ast, param):
        return None
    
    def visitArrayCell(self, ast, param):
        return None
    
    def visitFieldAccess(self, ast, param):
        return None
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitAssign(self, ast, param):
        return None
    
    def visitCallStmt(self, ast, param):
        return None
    
    def visitIntLiteral(self, ast, param):
        return None
    
    def visitFloatLiteral(self, ast, param):
        return None
    
    def visitBooleanLiteral(self, ast, param):
        return None
    
    def visitStringLiteral(self, ast, param):
        return None
    
    def visitNullLiteral(self, ast, param):
        return None
    
    def visitSelfLiteral(self, ast, param):
        return None 

    def visitArrayLiteral(self, ast, param):
        return None

class StaticChecker(BaseVisitor):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        c = GlobalEnv().visit(ast, {})
        c['curr'] = [None, None]
        c['vlc'] = []
        c['loop'] = 0
        return [self.visit(x,c) for x in ast.decl]

    def visitClassDecl(self,ast, c): 
        c['curr'][0] = ast.classname.name
        if ast.parentname:
            if not ast.parentname.name in c.keys():
                raise Undeclared(Class(),ast.parentname.name)
        [self.visit(x,c) for x in ast.memlist]
        c['curr'][0] = None
    
    def visitAttributeDecl(self, ast, c):
        c['curr'][1] = None
        return self.visit(ast.decl,c)
    
    def visitVarDecl(self, ast, c):   
        name = ast.variable.name
        typ = self.visit(ast.varType,c)
        if ast.varInit: 
            value = self.visit(ast.varInit,c)
            if (type(value['type']) is tuple) and (value['type'][2] == 'static'):
                raise Undeclared(Identifier(),value['type'][1])
        if c['curr'][1]:
            if name in c['vlc'][-1].keys(): raise Redeclared(Variable(),name)
            c['vlc'][-1].update({name: {'type': typ, 'isfinal': False}})
    
    def visitConstDecl(self, ast, c):
        name = ast.constant.name
        typ = self.visit(ast.constType,c)
        if typ == 'void': raise TypeMismatchInConstant(ast)
        if not ast.value: raise IllegalConstantExpression(ast.value)
        value = self.visit(ast.value,c)
        if (type(value['type']) is tuple) and (value['type'][2] == 'static'):
            raise Undeclared(Identifier(),value['type'][1])
        if not value['isfinal']: raise IllegalConstantExpression(ast.value)
        if c['curr'][1]:
            if name in c['vlc'][-1].keys(): raise Redeclared(Constant(),name)
            c['vlc'][-1].update({name: {'type': typ, 'isfinal': True}})
        if typ != value['type']:
            if typ == 'float' and value['type'] == 'int': return
            if (type(typ) is tuple) and (type(value['type']) is tuple):
                if typ[1] == value['type'][1]: return
                temp = c[value['type'][1]]['parent']
                while temp:
                    if temp == typ[1]: return
                    temp = c[temp]['parent']
            if (type(typ) is dict) and (type(value['type']) is dict):
                if typ['size'] == value['type']['size']:
                    ar = typ['eleType']
                    pa = value['type']['eleType']
                    if ar == 'float' and pa == 'int': return
                    if (type(ar) is tuple) and (type(pa) is tuple):
                        if ar[1] == pa[1]: return
                        temp = c[pa[1]]['parent']
                        while temp:
                            if temp == ar[1]: return
                            temp = c[temp]['parent']
            raise TypeMismatchInConstant(ast)
    
    def visitMethodDecl(self, ast, c):
        c['curr'][1] = ast.name.name
        self.visit(ast.body,c)
        c['curr'][1] = None
    
    def visitBlock(self, ast, c):
        c['vlc'] += [{}]
        [self.visit(x,c) for x in ast.decl]
        [self.visit(x,c) for x in ast.stmt]
        c['vlc'].pop(-1)
    
    def visitStatic(self, ast, c):
        return 'static'
    
    def visitInstance(self, ast, c):
        return 'instance'
    
    def visitIntType(self, ast, c):
        return 'int'
    
    def visitFloatType(self, ast, c):
        return 'float'
    
    def visitBoolType(self, ast, c):
        return 'boolean'
    
    def visitStringType(self, ast, c):
        return 'string'
    
    def visitVoidType(self, ast, c):
        return 'void'
    
    def visitArrayType(self, ast, c):
        return {'eleType': self.visit(ast.eleType,c), 'size': ast.size}
    
    def visitClassType(self, ast, c):
        name = ast.classname.name
        if name not in c.keys(): raise Undeclared(Class(),name)
        return ('class',name,'instance')
    
    def visitId(self, ast, c):
        for x in range(len(c['vlc'])-1,-1,-1):
            if ast.name in c['vlc'][x].keys(): return c['vlc'][x][ast.name]
        if c['curr'][1]:
            param = c[c['curr'][0]]['mem'][c['curr'][1]]['param']
            if ast.name in param.keys(): return param[ast.name]
        if ast.name in c.keys(): return {'type': ('class',ast.name,'static'), 'isfinal': False}
        raise Undeclared(Identifier(),ast.name)
    
    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left,c)
        if (type(left['type']) is tuple) and (left['type'][2] == 'static'):
            raise Undeclared(Identifier(),left['type'][1])
        right = self.visit(ast.right,c)
        if (type(right['type']) is tuple) and (right['type'][2] == 'static'):
            raise Undeclared(Identifier(),right['type'][1])
        if left['isfinal'] and right['isfinal']: isfinal = True
        else: isfinal = False
        if ast.op in ('\\','%'):
            if left['type'] != 'int' or right['type'] != 'int':
                raise TypeMismatchInExpression(ast)
            return {'type': 'int', 'isfinal': isfinal}
        elif ast.op in ('+','-','*','/'):
            if (left['type'] not in ('int','float')) or (right['type'] not in ('int','float')):
                raise TypeMismatchInExpression(ast)
            if left['type'] != 'int' or right['type'] != 'int' or ast.op == '/':
                return {'type': 'float', 'isfinal': isfinal}
            else: return {'type': 'int', 'isfinal': isfinal}
        elif ast.op in ('&&','||'):
            if left['type'] != 'boolean' or right['type'] != 'boolean':
                raise TypeMismatchInExpression(ast)
            return {'type': 'boolean', 'isfinal': isfinal}
        elif ast.op in ('==','!='):
            if left['type'] == right['type']:
                if left['type'] in ('int','boolean'):
                    return {'type': 'boolean', 'isfinal': isfinal}
            raise TypeMismatchInExpression(ast)
        elif ast.op in ('>','<','>=','<='):
            if (left['type'] not in ('int','float')) or (right['type'] not in ('int','float')):
                raise TypeMismatchInExpression(ast)
            return {'type': 'boolean', 'isfinal': isfinal} 
        elif ast.op == '^':
            if left['type'] != 'string' or right['type'] != 'string':
                raise TypeMismatchInExpression(ast)
            return {'type': 'string', 'isfinal': isfinal}
    
    def visitUnaryOp(self, ast, c):
        body = self.visit(ast.body,c)
        if (type(body['type']) is tuple) and (body['type'][2] == 'static'):
            raise Undeclared(Identifier(),body['type'][1])
        if ast.op in ('+','-'):
            if body['type'] not in ('int','float'):
                raise TypeMismatchInExpression(ast)
            return body
        elif ast.op == '!':
            if body['type'] != 'boolean':
                raise TypeMismatchInExpression(ast)
            return body
    
    def visitCallExpr(self, ast, c):
        obj = self.visit(ast.obj,c)
        name = ast.method.name
        param = [self.visit(x,c) for x in ast.param]
        if type(obj['type']) is tuple:
            temp = obj['type'][1]
            while temp:
                if name in c[temp]['mem'].keys():
                    tp = c[temp]['mem'][name]
                    if ('returnType' not in tp.keys()): 
                        if tp['kind'] == 'static': raise TypeMismatchInExpression(ast)
                        else: raise Undeclared(Method(),name)
                    elif tp['kind'] != obj['type'][2]: raise IllegalMemberAccess(ast)
                    if tp['returnType'] == 'void': raise TypeMismatchInExpression(ast)
                    if len(param) == len(tp['param']):
                        for para, args in zip(param, tp['param'].values()):
                            if para['type'] != args['type']:   
                                if args['type'] == 'float' and para['type'] == 'int': continue
                                if (type(args['type']) is tuple) and (type(para['type']) is tuple):
                                    if args['type'][1] == para['type'][1]: continue
                                    temp = c[para['type'][1]]['parent']
                                    b = False
                                    while temp:
                                        if temp == args['type'][1]: 
                                            b = True
                                            break
                                        temp = c[temp]['parent']
                                    if b: continue
                                if (type(args['type']) is dict) and (type(para['type']) is dict):
                                    if args['type']['size'] == para['type']['size']:
                                        ar = args['type']['eleType']
                                        pa = para['type']['eleType']
                                        if ar == 'float' and pa == 'int': continue
                                        if (type(ar) is tuple) and (type(pa) is tuple):
                                            if ar[1] == pa[1]: continue
                                            temp = c[pa[1]]['parent']
                                            b = False
                                            while temp:
                                                if temp == ar[1]: 
                                                    b = True
                                                    break
                                                temp = c[temp]['parent']
                                            if b: continue
                                raise TypeMismatchInExpression(ast)
                        return {'type': tp['returnType'], 'isfinal': False}
                    else: raise TypeMismatchInExpression(ast)
                temp = c[temp]['parent']       
            raise Undeclared(Method(),name)
        else: raise TypeMismatchInExpression(ast)
    
    def visitNewExpr(self, ast, c):
        name = ast.classname.name
        if name not in c.keys(): raise Undeclared(Class(),name)
        param = [self.visit(x,c) for x in ast.param]
        if '<init>' in c[name]['mem']:
            iparam = c[name]['mem']['<init>']['param']
            if len(param) == len(iparam):
                for para, args in zip(param, iparam.values()):
                    if para['type'] != args['type']:
                        if args['type'] == 'float' and para['type'] == 'int': continue
                        if (type(args['type']) is tuple) and (type(para['type']) is tuple):
                            temp = c[para['type'][1]]['parent']
                            b = False
                            while temp:
                                if temp == args['type'][1]: 
                                    b = True
                                    break
                                temp = c[temp]['parent']
                            if b: continue
                        if (type(args['type']) is dict) and (type(para['type']) is dict):
                            if args['type']['size'] == para['type']['size']:
                                ar = args['type']['eleType']
                                pa = para['type']['eleType']
                                if ar == 'float' and pa == 'int': continue
                                if (type(ar) is tuple) and (type(pa) is tuple):
                                    if ar[1] == pa[1]: continue
                                    temp = c[pa[1]]['parent']
                                    b = False
                                    while temp:
                                        if temp == ar[1]: 
                                            b = True
                                            break
                                        temp = c[temp]['parent']
                                    if b: continue
                        raise TypeMismatchInExpression(ast)
                return {'type': ('class',name,'instance'), 'isfinal': False}
            else: raise TypeMismatchInExpression(ast)
        else:
            if len(param) == 0:
                return {'type': ('class',name,'instance'), 'isfinal': False}
            raise TypeMismatchInExpression(ast)
    
    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr,c)
        if (type(arr['type']) is tuple) and (arr['type'][2] == 'static'):
            raise Undeclared(Identifier(),arr['type'][1])
        idx = self.visit(ast.idx,c)
        if type(arr['type']) is dict:
            if idx['type'] == 'int':
                return {'type': arr['type']['eleType'], 'isfinal': arr['isfinal']}
        raise TypeMismatchInExpression(ast)
    
    def visitFieldAccess(self, ast, c):
        obj = self.visit(ast.obj,c)
        fieldname = ast.fieldname.name
        if type(obj['type']) is tuple:
            if obj['type'][2] == 'instance':
                temp = c['curr'][0]
                b = True
                while temp:
                    if (temp == obj['type'][1]) and b: b = False
                    if (not b) and (fieldname in c[temp]['mem'].keys()):
                        tp = c[temp]['mem'][fieldname]
                        if ('isfinal' not in tp.keys()): raise TypeMismatchInExpression(ast)
                        elif tp['kind'] == 'static': raise IllegalMemberAccess(ast)
                        if b != None: 
                            if obj['isfinal'] and tp['isfinal']: return tp
                            else: return {'type': tp['type'], 'isfinal': False}
                        else: raise Undeclared(Attribute(),fieldname)
                    temp = c[temp]['parent']
                    if (not temp) and b: 
                        b = None
                        temp = obj['type'][1]
                raise Undeclared(Attribute(),fieldname)
            else:
                temp = obj['type'][1]
                while temp:
                    if fieldname in c[temp]['mem'].keys():
                        tp = c[temp]['mem'][fieldname]
                        if ('isfinal' not in tp.keys()): raise TypeMismatchInExpression(ast)
                        elif tp['kind'] == 'instance': raise IllegalMemberAccess(ast)
                        if obj['isfinal'] and tp['isfinal']: return tp
                        else: return {'type': tp['type'], 'isfinal': False}
                    temp = c[temp]['parent']
                raise Undeclared(Attribute(),fieldname)
        else: raise TypeMismatchInExpression(ast)
    
    def visitIf(self, ast, c):
        expr = self.visit(ast.expr,c)
        if (type(expr['type']) is tuple) and (expr['type'][2] == 'static'):
            raise Undeclared(Identifier(),expr['type'][1])
        if expr['type'] != 'boolean': raise TypeMismatchInExpression(ast)
        self.visit(ast.thenStmt,c)
        if ast.elseStmt: self.visit(ast.elseStmt,c)
    
    def visitFor(self, ast, c):
        id = self.visit(ast.id,c)
        if (type(id['type']) is tuple) and (id['type'][2] == 'static'):
            raise Undeclared(Identifier(),id['type'][1])
        expr1 = self.visit(ast.expr1,c)
        expr2 = self.visit(ast.expr2,c)
        if id['type'] != 'int' or expr1['type'] != 'int' or expr2['type'] != 'int':
            raise TypeMismatchInExpression(ast)
        if id['isfinal']: raise CannotAssignToConstant(Assign(ast.id,ast.expr1))
        c['loop'] += 1
        self.visit(ast.loop,c)
        c['loop'] -= 1
    
    def visitContinue(self, ast, c):
        if c['loop'] == 0: raise MustInLoop(ast)
    
    def visitBreak(self, ast, c):
        if c['loop'] == 0: raise MustInLoop(ast)
    
    def visitReturn(self, ast, c):
        expr = self.visit(ast.expr,c)
        if (type(expr['type']) is tuple) and (expr['type'][2] == 'static'):
            raise Undeclared(Identifier(),expr['type'][1])
        rtt = c[c['curr'][0]]['mem'][c['curr'][1]]['returnType']
        if rtt != expr['type']:
            if rtt == 'float' and expr['type'] == 'int': return
            if (type(rtt) is tuple) and (type(expr['type']) is tuple):
                if rtt[1] == expr['type'][1]: return
                temp = c[expr['type'][1]]['parent']
                while temp:
                    if temp == rtt[1]: return
                    temp = c[temp]['parent']
            if (type(rtt) is dict) and (type(expr['type']) is dict):
                if rtt['size'] == expr['type']['size']:
                    ar = rtt['eleType']
                    pa = expr['type']['eleType']
                    if ar == 'float' and pa == 'int': return
                    if (type(ar) is tuple) and (type(pa) is tuple):
                        if ar[1] == pa[1]: return
                        temp = c[pa[1]]['parent']
                        while temp:
                            if temp == ar[1]: return
                            temp = c[temp]['parent']
            raise TypeMismatchInStatement(ast)
    
    def visitAssign(self, ast, c):
        lhs = self.visit(ast.lhs,c)
        exp = self.visit(ast.exp,c)
        if (type(lhs['type']) is tuple) and (lhs['type'][2] == 'static'):
            raise Undeclared(Identifier(),lhs['type'][1])
        if (type(exp['type']) is tuple) and (exp['type'][2] == 'static'):
            raise Undeclared(Identifier(),exp['type'][1])
        if lhs['isfinal']: raise CannotAssignToConstant(ast)
        if lhs['type'] == 'void': raise TypeMismatchInStatement(ast)
        if lhs['type'] != exp['type']:
            if lhs['type'] == 'float' and exp['type'] == 'int': return
            if (type(lhs['type']) is tuple) and (type(exp['type']) is tuple):
                if lhs['type'][1] == exp['type'][1]: return
                temp = c[exp['type'][1]]['parent']
                while temp:
                    if temp == lhs['type'][1]: return
                    temp = c[temp]['parent']
            if (type(lhs['type']) is dict) and (type(exp['type']) is dict):
                if lhs['type']['size'] == exp['type']['size']:
                    ar = lhs['type']['eleType']
                    pa = exp['type']['eleType']
                    if ar == 'float' and pa == 'int': return
                    if (type(ar) is tuple) and (type(pa) is tuple):
                        if ar[1] == pa[1]: return
                        temp = c[pa[1]]['parent']
                        while temp:
                            if temp == ar[1]: return
                            temp = c[temp]['parent']
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, c):
        obj = self.visit(ast.obj,c)
        name = ast.method.name
        param = [self.visit(x,c) for x in ast.param]
        if type(obj['type']) is tuple:
            temp = obj['type'][1]
            while temp:
                if name in c[temp]['mem'].keys():
                    tp = c[temp]['mem'][name]
                    if ('returnType' not in tp.keys()): 
                        if tp['kind'] == 'static': raise TypeMismatchInStatement(ast)
                        else: raise Undeclared(Method(),name)
                    elif tp['kind'] != obj['type'][2]: raise IllegalMemberAccess(ast)
                    if tp['returnType'] != 'void': raise TypeMismatchInStatement(ast)
                    if len(param) == len(tp['param']):
                        for para, args in zip(param, tp['param'].values()):
                            if para['type'] != args['type']:
                                if args['type'] == 'float' and para['type'] == 'int': continue
                                if (type(args['type']) is tuple) and (type(para['type']) is tuple):
                                    if args['type'][1] == para['type'][1]: continue
                                    temp = c[para['type'][1]]['parent']
                                    b = False
                                    while temp:
                                        if temp == args['type'][1]: 
                                            b = True
                                            break
                                        temp = c[temp]['parent']
                                    if b: continue
                                if (type(args['type']) is dict) and (type(para['type']) is dict):
                                    if args['type']['size'] == para['type']['size']:
                                        ar = args['type']['eleType']
                                        pa = para['type']['eleType']
                                        if ar == 'float' and pa == 'int': continue
                                        if (type(ar) is tuple) and (type(pa) is tuple):
                                            if ar[1] == pa[1]: continue
                                            temp = c[pa[1]]['parent']
                                            b = False
                                            while temp:
                                                if temp == ar[1]: 
                                                    b = True
                                                    break
                                                temp = c[temp]['parent']
                                            if b: continue
                                raise TypeMismatchInStatement(ast)
                        return {'type': tp['returnType'], 'isfinal': False}
                    else: raise TypeMismatchInStatement(ast)
                temp = c[temp]['parent']
            raise Undeclared(Method(),name)
        else: raise TypeMismatchInStatement(ast)
    
    def visitIntLiteral(self, ast, c):
        return {'type': 'int', 'isfinal': True}
    
    def visitFloatLiteral(self, ast, c):
        return {'type': 'float', 'isfinal': True}
    
    def visitBooleanLiteral(self, ast, c):
        return {'type': 'boolean', 'isfinal': True}
    
    def visitStringLiteral(self, ast, c):
        return {'type': 'string', 'isfinal': True}
    
    def visitNullLiteral(self, ast, c):
        return {'type': 'null', 'isfinal': True}
    
    def visitSelfLiteral(self, ast, c):
        return {'type': ('class',c['curr'][0],'instance'), 'isfinal': True}

    def visitArrayLiteral(self, ast, c):
        typ = None
        for x in ast.value:
            if not typ: typ = self.visit(x,c)['type']
            else: 
                if typ != self.visit(x,c)['type']: raise IllegalArrayLiteral(ast)
        return {'type': {'eleType': typ, 'size': len(ast.value)}, 'isfinal': True}
                
    

