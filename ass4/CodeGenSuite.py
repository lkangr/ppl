import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input = """class BKoolClass {static void main() {io.writeInt(1);}}"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test2(self):
        input = """class BKoolClass {static void main() {io.writeInt(1+3);}}"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    def test3(self):
    	input = Program([ClassDecl(Id("BKoolClass"),
                            [MethodDecl(Static(),Id("main"),[],VoidType(),
                                Block([],[CallStmt(Id("io"),Id("writeInt"),[IntLiteral(1)])]))])])
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,502))

    def test4(self):
        input = Program([ClassDecl(Id("BKoolClass"),
                    [MethodDecl(Static(),Id("main"),[],VoidType(),
                        Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test5(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test6(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test7(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(2))),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test8(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(3))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test9(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),VarDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),VarDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test10(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test11(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test12(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),IntType(),IntLiteral(1))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test13(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),FloatType(),FloatLiteral(1.3))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test14(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test15(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeStr"),[StringLiteral('"ok"')])]))])])
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test16(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),BoolType(),BooleanLiteral(True)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeStr"),[StringLiteral('"ok"')])]))])])
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test17(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),BoolType(),BooleanLiteral(False)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeStr"),[StringLiteral('"ok"')])]))])])
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test18(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),BoolType(),BooleanLiteral(True)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeFloat"),[FloatLiteral(2.4)])]))])])
        expect = "2.4"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test19(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),BoolType(),BooleanLiteral(False)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"ok"')])]))])])
        expect = "ok\n"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test20(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(2.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),BoolType(),BooleanLiteral(False)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"ok"')])]))])])
        expect = "ok\n"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test21(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(3,BoolType()),ArrayLiteral([BooleanLiteral(False),BooleanLiteral(False),BooleanLiteral(True)])),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeStrLn"),[StringLiteral('"ok"')])]))])])
        expect = "ok\n"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test22(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(4.5)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeFloat"),[Id("a")])]))])])
        expect = "4.5"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test23(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(4.5)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeInt"),[ArrayCell(Id("b"),IntLiteral(2))])]))])])
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test24(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(4.5)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeFloat"),[FieldAccess(Id("BKoolClass"),Id("d"))])]))])])
        expect = "4.3"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test25(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(4.5)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeFloat"),[ArrayCell(FieldAccess(Id("BKoolClass"),Id("b")),IntLiteral(1))])]))])])
        expect = "4.5"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test26(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(4.5)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",FieldAccess(Id("BKoolClass"),Id("a")),FieldAccess(SelfLiteral(),Id("c")))])]))])])
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test27(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(4.5)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeFloat"),[UnaryOp("-",Id("a"))])]))])])
        expect = "-4.5"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test28(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(4.5)),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[CallStmt(Id("io"),Id("writeFloat"),[UnaryOp("+",Id("a"))])]))])])
        expect = "4.5"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test29(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType()),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[Assign(Id("a"),FloatLiteral(6.5)),CallStmt(Id("io"),Id("writeFloat"),[Id("a")])]))])])
        expect = "6.5"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test30(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType()),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[Assign(Id("a"),IntLiteral(6)),CallStmt(Id("io"),Id("writeFloat"),[Id("a")])]))])])
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test31(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType()),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[Assign(Id("a"),BinaryOp("+",IntLiteral(6),FloatLiteral(2.5))),CallStmt(Id("io"),Id("writeFloat"),[Id("a")])]))])])
        expect = "8.5"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test32(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType()),ConstDecl(Id("b"),ArrayType(4,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[Assign(Id("a"),BinaryOp("+",FloatLiteral(6.5),IntLiteral(2))),CallStmt(Id("io"),Id("writeFloat"),[Id("a")])]))])])
        expect = "8.5"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test33(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(2.3),FloatLiteral(4.5)]))),AttributeDecl(Instance(),VarDecl(Id("d"),FloatType(),FloatLiteral(4.3))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral('"aok"'),StringLiteral('"kao"')]))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("s"),IntType(),IntLiteral(1))],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Block([],[Assign(Id("s"),BinaryOp("+",Id("s"),IntLiteral(1)))])),CallStmt(Id("io"),Id("writeInt"),[Id("s")])]))])])
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test34(self):
        input = """class BKoolClass {static void main() {io.writeInt(1);}}"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test35(self):
        input = """class BKoolClass {static void main() {io.writeInt(1+3);}}"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test36(self):
    	input = Program([ClassDecl(Id("BKoolClass"),
                            [MethodDecl(Static(),Id("main"),[],VoidType(),
                                Block([],[CallStmt(Id("io"),Id("writeInt"),[IntLiteral(1)])]))])])
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,535))

    def test37(self):
        input = Program([ClassDecl(Id("BKoolClass"),
                    [MethodDecl(Static(),Id("main"),[],VoidType(),
                        Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test38(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test39(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test40(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(2))),AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test41(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(3))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def tes42(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),VarDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),VarDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test43(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test44(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test45(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),IntType(),IntLiteral(1))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test146(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),FloatType(),FloatLiteral(1.3))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,545))

    def test47(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeInt"),[BinaryOp("+",IntLiteral(1),IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test48(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(2)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeStr"),[StringLiteral('"ok"')])]))])])
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test49(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),BoolType(),BooleanLiteral(True)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeStr"),[StringLiteral('"ok"')])]))])])
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test50(self):
        input = Program([ClassDecl(Id("BKoolClass"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5))),AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(3))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(4))),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([ConstDecl(Id("c"),StringType(),StringLiteral('"aok"'))],[])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),BoolType(),BooleanLiteral(False)),ConstDecl(Id("b"),IntType(),IntLiteral(3))],[CallStmt(Id("io"),Id("writeStr"),[StringLiteral('"ok"')])]))])])
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input,expect,549))