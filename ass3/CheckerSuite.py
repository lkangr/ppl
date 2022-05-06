import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test1(self):
        input = Program([ClassDecl(Id("b"),[]),ClassDecl(Id("b"),[])])
        expect = "Redeclared Class: b"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test2(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("a"),FloatType()))])])
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test3(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),None))])])
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test4(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("s"),StringType())),MethodDecl(Instance(),Id("s"),[VarDecl(Id("a"),IntType()),VarDecl(Id("a"),IntType())],IntType(),Block([],[]))])])
        expect = "Redeclared Method: s"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test5(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("s"),StringType())),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("a"),IntType())],IntType(),Block([],[]))])])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test6(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("s"),StringType())),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([VarDecl(Id("a"),IntType())],[]))])])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test7(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("s"),StringType())),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([VarDecl(Id("s"),IntType()),ConstDecl(Id("b"),FloatType(),IntLiteral(2))],[]))])])
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test8(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("s"),StringType())),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("c"),IntType())],IntType(),Block([VarDecl(Id("s"),IntType()),ConstDecl(Id("b"),FloatType(),IntLiteral(2)),VarDecl(Id("b"),StringType())],[]))])])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test9(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("s"),StringType())),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("c"),IntType())],IntType(),Block([VarDecl(Id("s"),IntType()),ConstDecl(Id("foo"),FloatType(),IntLiteral(2)),ConstDecl(Id("s"),StringType(),None)],[]))])])
        expect = "Redeclared Constant: s"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test10(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("s"),StringType())),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("c"),IntType())],IntType(),Block([],[])),MethodDecl(Static(),Id("foo"),[],FloatType(),Block([],[]))])])
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test11(self):
        input = Program([ClassDecl(Id("a"),[],Id("b"))])
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test12(self):
        input = Program([ClassDecl(Id("b"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),Id("c"))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([VarDecl(Id("b"),IntType())],[]))])])
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test13(self):
        input = Program([ClassDecl(Id("b"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([VarDecl(Id("b"),IntType(),Id("a")),VarDecl(Id("c"),IntType(),Id("b")),VarDecl(Id("d"),IntType(),Id("d"))],[]))])])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test14(self):
        input = Program([ClassDecl(Id("b"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([VarDecl(Id("b"),IntType(),BinaryOp("+",IntLiteral(12),Id("c")))],[]))])])
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test15(self):
        input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([VarDecl(Id("c"),ClassType(Id("a")),NewExpr(Id("d"),[]))],[]))])])
        expect = "Undeclared Class: d"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test16(self):
        input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],IntType(),Block([VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[Assign(Id("b"),Id("d"))]))])])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test17(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType())],[For(Id("i"),IntLiteral(1),IntLiteral(5),True,Block([VarDecl(Id("k"),IntType(),IntLiteral(6))],[Assign(Id("j"),Id("k")),Assign(Id("k"),Id("m"))]))]))])])
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test18(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1)),VarDecl(Id("j"),IntType(),IntLiteral(2))],[If(BinaryOp(">",Id("i"),Id("j")),Block([],[Return(BinaryOp("*",Id("j"),Id("k")))]))]))])])
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test19(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("arr"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),FloatLiteral(4.5)]))],[]))])])
        expect = 'Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),FloatLit(4.5)]'
        self.assertTrue(TestChecker.test(input,expect,418))

    def test20(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("b"),IntType(),BinaryOp("%",FloatLiteral(6.5),IntLiteral(4)))],[]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(%,FloatLit(6.5),IntLit(4))'
        self.assertTrue(TestChecker.test(input,expect,419))

    def test21(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("b"),IntType(),BinaryOp("+",FloatLiteral(6.5),BooleanLiteral(True)))],[]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(+,FloatLit(6.5),BooleanLit(True))'
        self.assertTrue(TestChecker.test(input,expect,420))

    def test22(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("b"),IntType(),BinaryOp("%",IntLiteral(15),BinaryOp("/",IntLiteral(30),IntLiteral(3))))],[]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(%,IntLit(15),BinaryOp(/,IntLit(30),IntLit(3)))'
        self.assertTrue(TestChecker.test(input,expect,421))

    def test23(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp("==",IntLiteral(22),BooleanLiteral(True)),Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(==,IntLit(22),BooleanLit(True))'
        self.assertTrue(TestChecker.test(input,expect,422))

    def test24(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp("!=",StringLiteral('"hh"'),StringLiteral('"hh"')),Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(!=,StringLit("hh"),StringLit("hh"))'
        self.assertTrue(TestChecker.test(input,expect,423))

    def test25(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp("==",StringLiteral('"hh"'),BinaryOp(">=",FloatLiteral(6.7),IntLiteral(4))),Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(==,StringLit("hh"),BinaryOp(>=,FloatLit(6.7),IntLit(4)))'
        self.assertTrue(TestChecker.test(input,expect,424))

    def test26(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp("==",IntLiteral(45),BinaryOp(">",IntLiteral(6),BooleanLiteral(False))),Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(>,IntLit(6),BooleanLit(False))'
        self.assertTrue(TestChecker.test(input,expect,425))

    def test27(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("b"),StringType(),BinaryOp("^",StringLiteral('"first "'),IntLiteral(1)))],[]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(^,StringLit("first "),IntLit(1))'
        self.assertTrue(TestChecker.test(input,expect,426))

    def test28(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("m"),BoolType(),BooleanLiteral(True)),VarDecl(Id("n"),IntType(),UnaryOp("-",Id("m")))],[]))])])
        expect = 'Type Mismatch In Expression: UnaryOp(-,Id(m))'
        self.assertTrue(TestChecker.test(input,expect,427))

    def test29(self):
        input = Program([ClassDecl(Id("a"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(5))],[If(UnaryOp("!",Id("a")),Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: UnaryOp(!,Id(a))'
        self.assertTrue(TestChecker.test(input,expect,428))

    def test30(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(5)),VarDecl(Id("b"),IntType(),ArrayCell(Id("a"),IntLiteral(3)))],[]))])])
        expect = 'Type Mismatch In Expression: ArrayCell(Id(a),IntLit(3))'
        self.assertTrue(TestChecker.test(input,expect,429))

    def test31(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("c"),FloatType(),FloatLiteral(2.3)),VarDecl(Id("b"),IntType(),ArrayCell(Id("a"),Id("c")))],[]))])])
        expect = 'Type Mismatch In Expression: ArrayCell(Id(a),Id(c))'
        self.assertTrue(TestChecker.test(input,expect,430))

    def test32(self):
        input = Program([ClassDecl(Id("ttt"),[]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[IntLiteral(3)]))],[]))])])
        expect = 'Type Mismatch In Expression: NewExpr(Id(ttt),[IntLit(3)])'
        self.assertTrue(TestChecker.test(input,expect,431))

    def test33(self):
        input = Program([ClassDecl(Id("ttt"),[MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],VoidType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("a"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[IntLiteral(3),FloatLiteral(4.5)]))],[]))])])
        expect = 'Type Mismatch In Expression: NewExpr(Id(ttt),[IntLit(3),FloatLit(4.5)])'
        self.assertTrue(TestChecker.test(input,expect,432))

    def test34(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),IntType(),FieldAccess(Id("t"),Id("b")))],[]))])])
        expect = 'Undeclared Attribute: b'
        self.assertTrue(TestChecker.test(input,expect,433))

    def test35(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),IntType(),FieldAccess(Id("t"),Id("a")))],[]))])])
        expect = 'Illegal Member Access: FieldAccess(Id(t),Id(a))'
        self.assertTrue(TestChecker.test(input,expect,434))

    def test36(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),IntType(),FieldAccess(Id("ttt"),Id("b")))],[]))])])
        expect = 'Illegal Member Access: FieldAccess(Id(ttt),Id(b))'
        self.assertTrue(TestChecker.test(input,expect,435))

    def test37(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),IntType(),FieldAccess(Id("t"),Id("foo")))],[]))],Id("ttt"))])
        expect = 'Type Mismatch In Expression: FieldAccess(Id(t),Id(foo))'
        self.assertTrue(TestChecker.test(input,expect,436))

    def test38(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("foo"),[],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),IntType(),FieldAccess(Id("ttt"),Id("foo")))],[]))],Id("ttt"))])
        expect = 'Type Mismatch In Expression: FieldAccess(Id(ttt),Id(foo))'
        self.assertTrue(TestChecker.test(input,expect,437))

    def test39(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("foo"),[],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("m"),FloatType()),VarDecl(Id("a"),IntType(),FieldAccess(Id("m"),Id("foo")))],[]))],Id("ttt"))])
        expect = 'Type Mismatch In Expression: FieldAccess(Id(m),Id(foo))'
        self.assertTrue(TestChecker.test(input,expect,438))

    def test40(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("foo"),[],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("m"),FloatType()),VarDecl(Id("a"),IntType(),CallExpr(Id("m"),Id("foo"),[]))],[]))],Id("ttt"))])
        expect = 'Type Mismatch In Expression: CallExpr(Id(m),Id(foo),[])'
        self.assertTrue(TestChecker.test(input,expect,439))

    def test41(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("foo"),[],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),IntType(),CallExpr(Id("t"),Id("foo"),[]))],[]))],Id("ttt"))])
        expect = 'Illegal Member Access: CallExpr(Id(t),Id(foo),[])'
        self.assertTrue(TestChecker.test(input,expect,440))

    def test42(self):
        input = Program([ClassDecl(Id("ttt"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),IntType(),CallExpr(Id("ttt"),Id("foo"),[]))],[]))],Id("ttt"))])
        expect = 'Illegal Member Access: CallExpr(Id(ttt),Id(foo),[])'
        self.assertTrue(TestChecker.test(input,expect,441))

    def test43(self):
        input = Program([ClassDecl(Id("ttt"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),StringType())],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),StringType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("g"),IntType(),CallExpr(Id("t"),Id("foo"),[]))],[]))],Id("ttt"))])
        expect = 'Type Mismatch In Expression: CallExpr(Id(t),Id(foo),[])'
        self.assertTrue(TestChecker.test(input,expect,442))

    def test44(self):
        input = Program([ClassDecl(Id("ttt"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),StringType())],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),StringType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("g"),IntType(),CallExpr(Id("t"),Id("foo"),[Id("a"),Id("b"),Id("a")]))],[]))],Id("ttt"))])
        expect = 'Type Mismatch In Expression: CallExpr(Id(t),Id(foo),[Id(a),Id(b),Id(a)])'
        self.assertTrue(TestChecker.test(input,expect,443))

    def test45(self):
        input = Program([ClassDecl(Id("ttt"),[MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),StringType())],IntType(),Block([],[]))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("t"),ClassType(Id("ttt")),NewExpr(Id("ttt"),[])),VarDecl(Id("a"),StringType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("g"),IntType(),CallExpr(Id("t"),Id("foo"),[IntLiteral(1),IntLiteral(2)]))],[]))],Id("ttt"))])
        expect = 'Type Mismatch In Expression: CallExpr(Id(t),Id(foo),[IntLit(1),IntLit(2)])'
        self.assertTrue(TestChecker.test(input,expect,444))

    def test46(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType()),ConstDecl(Id("x"),IntType(),None)],[]))])])
        expect = 'Illegal Constant Expression: None'
        self.assertTrue(TestChecker.test(input,expect,445))

    def test47(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1)),ConstDecl(Id("x"),IntType(),BinaryOp("+",IntLiteral(1),BinaryOp("-",IntLiteral(2),Id("i"))))],[]))])])
        expect = 'Illegal Constant Expression: BinaryOp(+,IntLit(1),BinaryOp(-,IntLit(2),Id(i)))'
        self.assertTrue(TestChecker.test(input,expect,446))

    def test48(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1)),ConstDecl(Id("x"),VoidType(),BinaryOp("+",IntLiteral(1),BinaryOp("-",IntLiteral(2),Id("i"))))],[]))])])
        expect = 'Type Mismatch In Constant Declaration: ConstDecl(Id(x),VoidType,BinaryOp(+,IntLit(1),BinaryOp(-,IntLit(2),Id(i))))'
        self.assertTrue(TestChecker.test(input,expect,447))

    def test49(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1)),ConstDecl(Id("x"),IntType(),FloatLiteral(1.2))],[]))])])
        expect = 'Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(1.2))'
        self.assertTrue(TestChecker.test(input,expect,448))

    def test50(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([ConstDecl(Id("i"),FloatType(),IntLiteral(1)),ConstDecl(Id("x"),IntType(),BinaryOp("+",IntLiteral(34),Id("i")))],[]))])])
        expect = 'Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,BinaryOp(+,IntLit(34),Id(i)))'
        self.assertTrue(TestChecker.test(input,expect,449))

    def test51(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([ConstDecl(Id("i"),FloatType(),IntLiteral(1))],[Assign(Id("i"),FloatLiteral(3.4))]))])])
        expect = 'Cannot Assign To Constant: AssignStmt(Id(i),FloatLit(3.4))'
        self.assertTrue(TestChecker.test(input,expect,450))

    def test52(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType())],[Assign(Id("i"),FloatLiteral(3.4))]))])])
        expect = 'Type Mismatch In Statement: AssignStmt(Id(i),FloatLit(3.4))'
        self.assertTrue(TestChecker.test(input,expect,451))

    def test53(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),ArrayType(4,FloatType()))],[Assign(Id("i"),ArrayLiteral([IntLiteral(3),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6)]))]))])])
        expect = 'Type Mismatch In Statement: AssignStmt(Id(i),[IntLit(3),IntLit(2),IntLit(4),IntLit(5),IntLit(6)])'
        self.assertTrue(TestChecker.test(input,expect,452))

    def test54(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),ArrayType(5,BoolType()))],[Assign(Id("i"),ArrayLiteral([IntLiteral(3),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6)]))]))])])
        expect = 'Type Mismatch In Statement: AssignStmt(Id(i),[IntLit(3),IntLit(2),IntLit(4),IntLit(5),IntLit(6)])'
        self.assertTrue(TestChecker.test(input,expect,453))

    def test55(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(IntLiteral(4),Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: If(IntLit(4),Block([],[]))'
        self.assertTrue(TestChecker.test(input,expect,454))

    def test56(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),FloatType())],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: For(Id(i),IntLit(1),IntLit(10),True,Block([],[])])'
        self.assertTrue(TestChecker.test(input,expect,455))

    def test57(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),FloatType())],[For(Id("i"),IntLiteral(1),Id("j"),True,Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: For(Id(i),IntLit(1),Id(j),True,Block([],[])])'
        self.assertTrue(TestChecker.test(input,expect,456))

    def test58(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([ConstDecl(Id("i"),IntType(),IntLiteral(1))],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Block([],[]))]))])])
        expect = 'Cannot Assign To Constant: AssignStmt(Id(i),IntLit(1))'
        self.assertTrue(TestChecker.test(input,expect,457))

    def test59(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1))],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Block([],[])),Break()]))])])
        expect = 'Break Not In Loop'
        self.assertTrue(TestChecker.test(input,expect,458))

    def test60(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1))],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Block([],[])),Continue()]))])])
        expect = 'Continue Not In Loop'
        self.assertTrue(TestChecker.test(input,expect,459))

    def test61(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1))],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Block([],[Return(FloatLiteral(4.5))]))]))])])
        expect = 'Type Mismatch In Statement: Return(FloatLit(4.5))'
        self.assertTrue(TestChecker.test(input,expect,460))

    def test62(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),CallExpr(SelfLiteral(),Id("func"),[]))],[]))])])
        expect = 'Undeclared Method: func'
        self.assertTrue(TestChecker.test(input,expect,461))

    def test63(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[CallStmt(SelfLiteral(),Id("a"),[])]))])])
        expect = 'Type Mismatch In Statement: Call(Self(),Id(a),[])'
        self.assertTrue(TestChecker.test(input,expect,462))

    def test64(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[CallStmt(SelfLiteral(),Id("b"),[IntLiteral(1)])]))])])
        expect = 'Undeclared Method: b'
        self.assertTrue(TestChecker.test(input,expect,463))

    def test65(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[CallStmt(SelfLiteral(),Id("a"),[IntLiteral(1)])]))])])
        expect = 'Type Mismatch In Statement: Call(Self(),Id(a),[IntLit(1)])'
        self.assertTrue(TestChecker.test(input,expect,464))

    def test66(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),IntType())],VoidType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[CallStmt(SelfLiteral(),Id("a"),[FloatLiteral(1.4)])]))])])
        expect = 'Type Mismatch In Statement: Call(Self(),Id(a),[FloatLit(1.4)])'
        self.assertTrue(TestChecker.test(input,expect,465))

    def test67(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),FloatType())],VoidType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[CallStmt(SelfLiteral(),Id("a"),[BinaryOp(">",IntLiteral(1),IntLiteral(2))])]))])])
        expect = 'Type Mismatch In Statement: Call(Self(),Id(a),[BinaryOp(>,IntLit(1),IntLit(2))])'
        self.assertTrue(TestChecker.test(input,expect,466))

    def test68(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),FloatType())],VoidType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("i"),IntType(),CallExpr(SelfLiteral(),Id("a"),[FloatLiteral(2.3)]))],[]))])])
        expect = 'Type Mismatch In Expression: CallExpr(Self(),Id(a),[FloatLit(2.3)])'
        self.assertTrue(TestChecker.test(input,expect,467))

    def test69(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),FloatType())],VoidType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType()),VarDecl(Id("z"),FloatType()),VarDecl(Id("m"),FloatType()),VarDecl(Id("k"),IntType())],[Assign(Id("k"),BinaryOp("/",BinaryOp("*",BinaryOp("+",Id("x"),Id("y")),Id("k")),Id("z")))]))])])
        expect = 'Type Mismatch In Statement: AssignStmt(Id(k),BinaryOp(/,BinaryOp(*,BinaryOp(+,Id(x),Id(y)),Id(k)),Id(z)))'
        self.assertTrue(TestChecker.test(input,expect,468))

    def test70(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("i"),FloatType())],VoidType(),Block([],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType()),ConstDecl(Id("d"),FloatType(),BinaryOp("/",Id("x"),Id("y")))],[]))])])
        expect = 'Illegal Constant Expression: BinaryOp(/,Id(x),Id(y))'
        self.assertTrue(TestChecker.test(input,expect,469))

    def test71(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType())],[Block([VarDecl(Id("m"),IntType()),VarDecl(Id("n"),IntType()),VarDecl(Id("n"),FloatType())],[])]))])])
        expect = 'Redeclared Variable: n'
        self.assertTrue(TestChecker.test(input,expect,470))

    def test72(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType()),VarDecl(Id("f"),IntType())],[Block([VarDecl(Id("m"),IntType()),VarDecl(Id("n"),IntType()),ConstDecl(Id("c"),FloatType(),Id("f"))],[])]))])])
        expect = 'Illegal Constant Expression: Id(f)'
        self.assertTrue(TestChecker.test(input,expect,471))

    def test73(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType()),VarDecl(Id("f"),IntType())],[Return(BinaryOp("/",Id("m"),Id("f")))]))])])
        expect = 'Type Mismatch In Statement: Return(BinaryOp(/,Id(m),Id(f)))'
        self.assertTrue(TestChecker.test(input,expect,472))

    def test74(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([],[Continue()]))])])
        expect = 'Continue Not In Loop'
        self.assertTrue(TestChecker.test(input,expect,473))

    def test75(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([],[For(Id("x"),IntLiteral(1),IntLiteral(10),True,Block([],[]))]))])])
        expect = 'Undeclared Identifier: x'
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test76(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([ConstDecl(Id("x"),IntType(),None)],[For(Id("x"),IntLiteral(1),IntLiteral(10),True,Block([],[]))]))])])
        expect = 'Illegal Constant Expression: None'
        self.assertTrue(TestChecker.test(input,expect,475))

    def test77(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([ConstDecl(Id("x"),IntType(),IntLiteral(1))],[For(Id("x"),IntLiteral(1),IntLiteral(10),True,Block([],[]))]))])])
        expect = 'Cannot Assign To Constant: AssignStmt(Id(x),IntLit(1))'
        self.assertTrue(TestChecker.test(input,expect,476))

    def test78(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("x"),IntType(),IntLiteral(1))],[For(Id("x"),IntLiteral(1),FloatLiteral(1.0),True,Block([],[]))]))])])
        expect = 'Type Mismatch In Expression: For(Id(x),IntLit(1),FloatLit(1.0),True,Block([],[])])'
        self.assertTrue(TestChecker.test(input,expect,477))

    def test79(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("x"),IntType(),IntLiteral(1))],[For(Id("x"),IntLiteral(1),IntLiteral(10),True,Block([],[Assign(Id("x"),FloatLiteral(20.5))]))]))])])
        expect = 'Type Mismatch In Statement: AssignStmt(Id(x),FloatLit(20.5))'
        self.assertTrue(TestChecker.test(input,expect,478))

    def test80(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("x"),IntType(),IntLiteral(1))],[For(Id("x"),IntLiteral(1),IntLiteral(10),True,Block([],[Assign(Id("abc"),IntLiteral(5))]))]))])])
        expect = 'Undeclared Identifier: abc'
        self.assertTrue(TestChecker.test(input,expect,479))

    def test81(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())],[For(Id("x"),IntLiteral(1),IntLiteral(10),True,Block([],[For(Id("y"),IntLiteral(1),IntLiteral(10),True,Block([ConstDecl(Id("z"),IntType(),BinaryOp("+",Id("x"),Id("y")))],[]))]))]))])])
        expect = 'Illegal Constant Expression: BinaryOp(+,Id(x),Id(y))'
        self.assertTrue(TestChecker.test(input,expect,480))

    def test82(self):
        input = Program([ClassDecl(Id("abc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())],[For(Id("x"),IntLiteral(1),IntLiteral(10),True,Block([],[For(Id("y"),IntLiteral(1),IntLiteral(10),True,Block([VarDecl(Id("z"),IntType())],[Assign(Id("z"),BinaryOp("/",Id("x"),Id("y")))]))]))]))])])
        expect = 'Type Mismatch In Statement: AssignStmt(Id(z),BinaryOp(/,Id(x),Id(y)))'
        self.assertTrue(TestChecker.test(input,expect,481))

    def test83(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("x"),[VarDecl(Id("i"),IntType()),VarDecl(Id("y"),StringType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("a"),[],IntType(),Block([ConstDecl(Id("m"),IntType(),CallExpr(SelfLiteral(),Id("x"),[IntLiteral(1),StringLiteral('"1"')]))],[]))])])
        expect = 'Illegal Constant Expression: CallExpr(Self(),Id(x),[IntLit(1),StringLit("1")])'
        self.assertTrue(TestChecker.test(input,expect,482))

    def test84(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("x"),[VarDecl(Id("i"),IntType()),VarDecl(Id("y"),StringType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType())],[Assign(Id("m"),CallExpr(SelfLiteral(),Id("x"),[IntLiteral(1),BinaryOp("^",Id("m"),StringLiteral('"k"'))]))]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(^,Id(m),StringLit("k"))'
        self.assertTrue(TestChecker.test(input,expect,483))

    def test85(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("x"),[VarDecl(Id("i"),ArrayType(3,FloatType())),VarDecl(Id("y"),StringType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType())],[Assign(Id("m"),CallExpr(SelfLiteral(),Id("x"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),IntLiteral(4)]))]))])])
        expect = 'Type Mismatch In Expression: CallExpr(Self(),Id(x),[[IntLit(1),IntLit(2),IntLit(3)],IntLit(4)])'
        self.assertTrue(TestChecker.test(input,expect,484))

    def test86(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("x"),[VarDecl(Id("i"),ArrayType(3,FloatType())),VarDecl(Id("y"),StringType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType()),ConstDecl(Id("z"),FloatType(),BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),IntLiteral(3))),BinaryOp("%",BinaryOp("/",IntLiteral(4),IntLiteral(5)),Id("m"))))],[]))])])
        expect = 'Type Mismatch In Expression: BinaryOp(%,BinaryOp(/,IntLit(4),IntLit(5)),Id(m))'
        self.assertTrue(TestChecker.test(input,expect,485))

    def test87(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("x"),[VarDecl(Id("i"),ArrayType(3,FloatType())),VarDecl(Id("y"),StringType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType()),ConstDecl(Id("z"),FloatType(),BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),IntLiteral(3))),BinaryOp("/",IntLiteral(4),BinaryOp("%",IntLiteral(5),Id("m")))))],[]))])])
        expect = 'Illegal Constant Expression: BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),BinaryOp(%,IntLit(5),Id(m))))'
        self.assertTrue(TestChecker.test(input,expect,486))

    def test88(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("x"),[VarDecl(Id("i"),ArrayType(3,FloatType())),VarDecl(Id("y"),StringType())],IntType(),Block([],[])),MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),IntType())],[Assign(Id("m"),BinaryOp("/",Id("m"),Id("m")))]))])])
        expect = 'Type Mismatch In Statement: AssignStmt(Id(m),BinaryOp(/,Id(m),Id(m)))'
        self.assertTrue(TestChecker.test(input,expect,487))

    def test89(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("m"),ArrayType(4,IntType())),ConstDecl(Id("n"),IntType(),ArrayCell(Id("m"),IntLiteral(2)))],[]))])])
        expect = 'Illegal Constant Expression: ArrayCell(Id(m),IntLit(2))'
        self.assertTrue(TestChecker.test(input,expect,488))

    def test90(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([ConstDecl(Id("m"),ArrayType(4,IntType()),None),ConstDecl(Id("n"),IntType(),ArrayCell(Id("m"),IntLiteral(2)))],[]))])])
        expect = 'Illegal Constant Expression: None'
        self.assertTrue(TestChecker.test(input,expect,489))

    def test91(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([ConstDecl(Id("m"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),ConstDecl(Id("n"),StringType(),ArrayCell(Id("m"),IntLiteral(2)))],[]))])])
        expect = 'Type Mismatch In Constant Declaration: ConstDecl(Id(n),StringType,ArrayCell(Id(m),IntLit(2)))'
        self.assertTrue(TestChecker.test(input,expect,490))

    def test92(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("c"),ClassType(Id("b")),NewExpr(Id("b"),[]))],[]))])])
        expect = 'Undeclared Class: b'
        self.assertTrue(TestChecker.test(input,expect,491))

    def test93(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("c"),ClassType(Id("abc")),NewExpr(Id("b"),[]))],[]))])])
        expect = 'Undeclared Class: b'
        self.assertTrue(TestChecker.test(input,expect,492))

    def test94(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("c"),ClassType(Id("abc")),NewExpr(Id("abc"),[IntLiteral(2)]))],[]))])])
        expect = 'Type Mismatch In Expression: NewExpr(Id(abc),[IntLit(2)])'
        self.assertTrue(TestChecker.test(input,expect,493))

    def test95(self):
        input = Program([ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("c"),ClassType(Id("abc")),Id("abc"))],[]))])])
        expect = 'Undeclared Identifier: abc'
        self.assertTrue(TestChecker.test(input,expect,494))

    def test96(self):
        input = Program([ClassDecl(Id("aaa"),[]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([ConstDecl(Id("c"),ClassType(Id("abc")),NewExpr(Id("aaa"),[]))],[]))],Id("aaa"))])
        expect = 'Illegal Constant Expression: NewExpr(Id(aaa),[])'
        self.assertTrue(TestChecker.test(input,expect,495))

    def test97(self):
        input = Program([ClassDecl(Id("aaa"),[]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([ConstDecl(Id("c"),ClassType(Id("aaa")),NewExpr(Id("abc"),[IntLiteral(1),IntLiteral(2)]))],[]))],Id("aaa"))])
        expect = 'Type Mismatch In Expression: NewExpr(Id(abc),[IntLit(1),IntLit(2)])'
        self.assertTrue(TestChecker.test(input,expect,496))

    def test98(self):
        input = Program([ClassDecl(Id("aaa"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([VarDecl(Id("b"),IntType(),FieldAccess(SelfLiteral(),Id("b"))),VarDecl(Id("a"),IntType(),FieldAccess(SelfLiteral(),Id("a")))],[]))],Id("aaa"))])
        expect = 'Type Mismatch In Expression: FieldAccess(Self(),Id(a))'
        self.assertTrue(TestChecker.test(input,expect,497))

    def test99(self):
        input = Program([ClassDecl(Id("aaa"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("c"),[],IntType(),Block([VarDecl(Id("b"),IntType(),FieldAccess(SelfLiteral(),Id("b"))),VarDecl(Id("a"),IntType(),FieldAccess(SelfLiteral(),Id("a")))],[]))],Id("aaa"))])
        expect = 'Illegal Member Access: FieldAccess(Self(),Id(a))'
        self.assertTrue(TestChecker.test(input,expect,498))

    def test100(self):
        input = Program([ClassDecl(Id("aaa"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))]),ClassDecl(Id("abc"),[MethodDecl(Instance(),Id("c"),[],IntType(),Block([VarDecl(Id("b"),IntType(),FieldAccess(SelfLiteral(),Id("b"))),VarDecl(Id("a"),IntType(),FieldAccess(Id("aaa"),Id("a"))),ConstDecl(Id("c"),IntType(),BinaryOp("/",Id("a"),Id("b")))],[]))],Id("aaa"))])
        expect = 'Illegal Constant Expression: BinaryOp(/,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input,expect,499))