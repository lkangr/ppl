import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test2(self):
        input = """class main {
            int a;
        }"""  
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
   
    def test3(self):
        input = """class main {
            int a;
            int b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
   
    def test4(self):
        input = "class a extends b {}"
        expect = str(Program([ClassDecl(Id("a"),[],Id("b"))]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test5(self):
        input = """class Ex {
            int my1Var;
        }"""
        expect = str(Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),VarDecl(Id("my1Var"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test6(self):
        input = """class Ex {
            final int x = 10;
        }"""
        expect = str(Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),IntLiteral(10)))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test7(self):
        input = """class cls {
            static float a;
        }"""
        expect = str(Program([ClassDecl(Id("cls"),[AttributeDecl(Static(),VarDecl(Id("a"),FloatType()))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test8(self):
        input = """class cls {
            static final string a = "hello";
        }"""
        expect = str(Program([ClassDecl(Id("cls"),[AttributeDecl(Static(),ConstDecl(Id("a"),StringType(),StringLiteral('"hello"')))])]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test9(self):
        input = """class Shape {
            final float c = 2e3;
            void main() {
                io.writeFloatLn(this.c);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),ConstDecl(Id("c"),FloatType(),FloatLiteral(2000.0))),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeFloatLn"),[FieldAccess(SelfLiteral(),
        Id("c"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test10(self):
        input = """class Shape {
            final float c = 2e3;
            static int b = 6;
            void main() {
                float a = b * c;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),ConstDecl(Id("c"),FloatType(),FloatLiteral(2e3))),
        AttributeDecl(Static(),VarDecl(Id("b"),IntType(),IntLiteral(6))),MethodDecl(Static(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("a"),FloatType(),BinaryOp("*",Id("b"),Id("c")))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test11(self):
        input = """class Shape {
            string func() {
                return "hello";
            }
            void main() {
                this.func();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("func"),[],StringType(),Block([],[Return(StringLiteral('"hello"'))])),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(SelfLiteral(),Id("func"),[])]))])]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test12(self):
        input = """class Shape {
            string func() {
                return "hello";
            }
            void main() {
                string str = this.func();
                io.writeStringLn(str);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("func"),[],StringType(),Block([],[Return(StringLiteral('"hello"'))])),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("str"),StringType(),CallExpr(SelfLiteral(),Id("func"),[]))],[CallStmt(Id("io"),
        Id("writeStringLn"),[Id("str")])]))])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test13(self):
        input = """class Shape {
            void main() {
                int x = 0, i;
                for i := 1 to 10 do
                    x := x + i;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("x"),IntType(),
        IntLiteral(0)),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,Assign(Id("x"),
        BinaryOp("+",Id("x"),Id("i"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test14(self):
        input = """class Shape {
            static int m = 3;
            void main() {
                int[3] x = {1,2,3};
                for i := 1 to 3 do
                    this.m := this.m + x[i];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Static(),VarDecl(Id("m"),IntType(),IntLiteral(3))),MethodDecl(Static(),
        Id("main"),[],VoidType(),Block([VarDecl(Id("x"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],
        [For(Id("i"),IntLiteral(1),IntLiteral(3),True,Assign(FieldAccess(SelfLiteral(),Id("m")),BinaryOp("+",FieldAccess(SelfLiteral(),
        Id("m")),ArrayCell(Id("x"),Id("i")))))]))])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test15(self):
        input = """class Shape {
            void main() {
                string a = "hello";
                string b = "world";
                string c = a + " " + b;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),StringType(),
        StringLiteral('"hello"')),VarDecl(Id("b"),StringType(),StringLiteral('"world"')),VarDecl(Id("c"),StringType(),BinaryOp("+",
        BinaryOp("+",Id("a"),StringLiteral('" "')),Id("b")))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test16(self):
        input = """class Shape {
            void main() {
                string a = "hello";
                string b = "world";
                string c;
                c := a ^ b;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),StringType(),
        StringLiteral('"hello"')),VarDecl(Id("b"),StringType(),StringLiteral('"world"')),VarDecl(Id("c"),StringType())],[Assign(Id("c"),
        BinaryOp("^",Id("a"),Id("b")))]))])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test17(self):
        input = """class Shape {
            void main() {
                int a = 3 + 4 / 2 - 4 * 6 \ 3;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        BinaryOp("-",BinaryOp("+",IntLiteral(3),BinaryOp("/",IntLiteral(4),IntLiteral(2))),BinaryOp("\\",BinaryOp("*",IntLiteral(4),
        IntLiteral(6)),IntLiteral(3))))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,316))
   
    def test18(self):
        input = """class Shape {
            void main() {
                int a;
                if 3 < 5 then a := 3;
                else a := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType())],
        [If(BinaryOp("<",IntLiteral(3),IntLiteral(5)),Assign(Id("a"),IntLiteral(3)),Assign(Id("a"),IntLiteral(5)))]))])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test19(self):
        input = """class Shape {
            void main() {
                int a;
                if 3 < 5 && 2 != 4 then a := 34 * 12;
                else a := 5 / 20;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType())],
        [If(BinaryOp("<",IntLiteral(3),BinaryOp("!=",BinaryOp("&&",IntLiteral(5),IntLiteral(2)),IntLiteral(4))),Assign(Id("a"),
        BinaryOp("*",IntLiteral(34),IntLiteral(12))),Assign(Id("a"),BinaryOp("/",IntLiteral(5),IntLiteral(20))))]))])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test20(self):
        input = """class Shape {
            void main() {
                int a = 1 + 2 - 3 * 4 / 5 \ 6;
                int b = -a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("\\",BinaryOp("/",BinaryOp("*",IntLiteral(3),IntLiteral(4)),
        IntLiteral(5)),IntLiteral(6)))),VarDecl(Id("b"),IntType(),UnaryOp("-",Id("a")))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test21(self):
        input = """class Shape {
            void main() {
                int i, s = 0;
                for i := 1 to 1000 do {
                    s := s + i;
                    if i > 50 then break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType()),
        VarDecl(Id("s"),IntType(),IntLiteral(0))],[For(Id("i"),IntLiteral(1),IntLiteral(1000),True,Block([],[Assign(Id("s"),
        BinaryOp("+",Id("s"),Id("i"))),If(BinaryOp(">",Id("i"),IntLiteral(50)),Break())]))]))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test22(self):
        input = """class Shape {
            void main() {
                int i, s = 0;
                for i := 1 to 1000 do {
                    s := s + i;
                    if i > 50 then break;
                    else continue;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType()),
        VarDecl(Id("s"),IntType(),IntLiteral(0))],[For(Id("i"),IntLiteral(1),IntLiteral(1000),True,Block([],[Assign(Id("s"),BinaryOp("+",
        Id("s"),Id("i"))),If(BinaryOp(">",Id("i"),IntLiteral(50)),Break(),Continue())]))]))])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test23(self):
        input = """class Shape {
            boolean istrue(boolean a) {
                if a == true then return true;
                else return false;
            }
            void main() {
                float a = 23.45e-67;
                if this.istrue(true) then a := a * a;
                else a := a / (a + a \ 2);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("istrue"),[VarDecl(Id("a"),BoolType())],BoolType(),Block([],
        [If(BinaryOp("==",Id("a"),BooleanLiteral(True)),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),MethodDecl(Static(),
        Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType(),FloatLiteral(23.45e-67))],[If(CallExpr(SelfLiteral(),Id("istrue"),
        [BooleanLiteral(True)]),Assign(Id("a"),BinaryOp("*",Id("a"),Id("a"))),Assign(Id("a"),BinaryOp("/",Id("a"),BinaryOp("+",Id("a"),
        BinaryOp("\\",Id("a"),IntLiteral(2))))))]))])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test24(self):
        input = """class Shape {
            void main() {
                io.writeStringLn("Hello World!");
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),
        Id("writeStringLn"),[StringLiteral('"Hello World!"')])]))])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test25(self):
        input = """class Shape {
            void main() {
                int a = 1, b = 2;
                if ! 3 < 5 || ! 6 > 9 && a == b then
                    io.writeStringLn("Hello World!");
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        IntLiteral(1)),VarDecl(Id("b"),IntType(),IntLiteral(2))],[If(BinaryOp(">",BinaryOp("<",UnaryOp("!",IntLiteral(3)),
        BinaryOp("||",IntLiteral(5),UnaryOp("!",IntLiteral(6)))),BinaryOp("==",BinaryOp("&&",IntLiteral(9),Id("a")),Id("b"))),
        CallStmt(Id("io"),Id("writeStringLn"),[StringLiteral('"Hello World!"')]))]))])]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test26(self):
        input = """class Parent {}
        class Shape extends Parent {
            void main() {
                int a = 1, b = 2;
                if ! 3 < 5 || ! 6 > 9 && a == b then
                    io.writeStringLn("Hello World!");
            }
        }"""
        expect = str(Program([ClassDecl(Id("Parent"),[]),ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("a"),IntType(),IntLiteral(1)),VarDecl(Id("b"),IntType(),IntLiteral(2))],[If(BinaryOp(">",BinaryOp("<",
        UnaryOp("!",IntLiteral(3)),BinaryOp("||",IntLiteral(5),UnaryOp("!",IntLiteral(6)))),BinaryOp("==",BinaryOp("&&",IntLiteral(9),
        Id("a")),Id("b"))),CallStmt(Id("io"),Id("writeStringLn"),[StringLiteral('"Hello World!"')]))]))],Id("Parent"))]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test27(self):
        input = """class Parent {
            final static int a = 5;
        }
        class Shape extends Parent {
            void main() {
                int a = 1;
                int b = a * Parent.a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Parent"),[AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(5)))]),ClassDecl(Id("Shape"),
        [MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(1)),VarDecl(Id("b"),IntType(),
        BinaryOp("*",Id("a"),FieldAccess(Id("Parent"),Id("a"))))],[]))],Id("Parent"))]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test28(self):
        input = """class Parent {
            static string func(string a, b) {
                return a ^ b;
            }
        }
        class Shape extends Parent {
            void main() {
                string c = "a", d = "b";
                string e = Parent.func(c, d);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Parent"),[MethodDecl(Static(),Id("func"),[VarDecl(Id("a"),StringType()),VarDecl(Id("b"),
        StringType())],StringType(),Block([],[Return(BinaryOp("^",Id("a"),Id("b")))]))]),ClassDecl(Id("Shape"),[MethodDecl(Static(),
        Id("main"),[],VoidType(),Block([VarDecl(Id("c"),StringType(),StringLiteral('"a"')),VarDecl(Id("d"),StringType(),StringLiteral('"b"')),
        VarDecl(Id("e"),StringType(),CallExpr(Id("Parent"),Id("func"),[Id("c"),Id("d")]))],[]))],Id("Parent"))]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test29(self):
        input = """class Parent {
            static string func(string a, b; boolean m) {
                if m then return a;
                else return b;
            }
        }
        class Shape extends Parent {
            void main() {
                string c = "a", d = "b";
                string e = Parent.func(c, d, false);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Parent"),[MethodDecl(Static(),Id("func"),[VarDecl(Id("a"),StringType()),VarDecl(Id("b"),
        StringType()),VarDecl(Id("m"),BoolType())],StringType(),Block([],[If(Id("m"),Return(Id("a")),Return(Id("b")))]))]),ClassDecl(Id("Shape"),
        [MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("c"),StringType(),StringLiteral('"a"')),VarDecl(Id("d"),
        StringType(),StringLiteral('"b"')),VarDecl(Id("e"),StringType(),CallExpr(Id("Parent"),Id("func"),[Id("c"),Id("d"),
        BooleanLiteral(False)]))],[]))],Id("Parent"))]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test30(self):
        input = """class Parent {
            static float func(float a; int b, c) {
                return a * (b + c);
            }
        }
        class Shape extends Parent {
            void main() {
                io.writeFloatLn(Parent.func(5.6,4,3));
            }
        }"""
        expect = str(Program([ClassDecl(Id("Parent"),[MethodDecl(Static(),Id("func"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType()),
        VarDecl(Id("c"),IntType())],FloatType(),Block([],[Return(BinaryOp("*",Id("a"),BinaryOp("+",Id("b"),Id("c"))))]))]),ClassDecl(Id("Shape"),
        [MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("Parent"),Id("func"),
        [FloatLiteral(5.6),IntLiteral(4),IntLiteral(3)])])]))],Id("Parent"))]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test31(self):
        input = """class Shape {
            static final int pi = 3.14;
            void main() {
                int x = 34;
                int s = x * x * this.pi;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Static(),ConstDecl(Id("pi"),IntType(),FloatLiteral(3.14))),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("x"),IntType(),IntLiteral(34)),VarDecl(Id("s"),IntType(),
        BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),FieldAccess(SelfLiteral(),Id("pi"))))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test32(self):
        input = """class Shape {
            void main() {
                int s = 0, i;
                for i := 100 downto 0 do
                    s := s - i;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),IntType(),
        IntLiteral(0)),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(100),IntLiteral(0),False,Assign(Id("s"),BinaryOp("-",
        Id("s"),Id("i"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test33(self):
        input = """class Shape {
            void main() {
                int s = 0;
                {
                    int s = 1;
                    {
                        int s = 2;
                    }
                    s := 3;
                }
                s := 4;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),IntType(),
        IntLiteral(0))],[Block([VarDecl(Id("s"),IntType(),IntLiteral(1))],[Block([VarDecl(Id("s"),IntType(),IntLiteral(2))],[]),
        Assign(Id("s"),IntLiteral(3))]),Assign(Id("s"),IntLiteral(4))]))])]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test34(self):
        input = """class Shape {
            int a() {
                return this.b();
            }
            int b() {
                return 5;
            }
            void main() {
                int b = this.a();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([],[Return(CallExpr(SelfLiteral(),
        Id("b"),[]))])),MethodDecl(Instance(),Id("b"),[],IntType(),Block([],[Return(IntLiteral(5))])),MethodDecl(Static(),Id("main"),
        [],VoidType(),Block([VarDecl(Id("b"),IntType(),CallExpr(SelfLiteral(),Id("a"),[]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test35(self):
        input = """class Shape {
            int a(float b) {
                int c = b \ 2;
                return c;
            }
            void main() {
                int a = this.a();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("a"),[VarDecl(Id("b"),FloatType())],IntType(),
        Block([VarDecl(Id("c"),IntType(),BinaryOp("\\",Id("b"),IntLiteral(2)))],[Return(Id("c"))])),MethodDecl(Static(),Id("main"),
        [],VoidType(),Block([VarDecl(Id("a"),IntType(),CallExpr(SelfLiteral(),Id("a"),[]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test36(self):
        input = """class shark {
            final int a = 3;
            static float b = 4.3e55;
        }
        class Shape {
            void main() {
                shark a = new shark();
                float b = a.a * a.b;
            }
        }"""
        expect = str(Program([ClassDecl(Id("shark"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),IntLiteral(3))),
        AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(4.3e+55)))]),ClassDecl(Id("Shape"),[MethodDecl(Static(),
        Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ClassType(Id("shark")),NewExpr(Id("shark"),[])),VarDecl(Id("b"),FloatType(),
        BinaryOp("*",FieldAccess(Id("a"),Id("a")),FieldAccess(Id("a"),Id("b"))))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test37(self):
        input = """class shark {
            final int a = 3;
            static float b = 4.3e55;
            float f() {
                return this.a * this.b;
            }
        }
        class Shape {
            void main() {
                shark a = new shark();
                float b = a.f();
            }
        }"""
        expect = str(Program([ClassDecl(Id("shark"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),IntLiteral(3))),
        AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(4.3e+55))),MethodDecl(Instance(),Id("f"),[],FloatType(),Block([],
        [Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("a")),FieldAccess(SelfLiteral(),Id("b"))))]))]),ClassDecl(Id("Shape"),
        [MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ClassType(Id("shark")),NewExpr(Id("shark"),[])),
        VarDecl(Id("b"),FloatType(),CallExpr(Id("a"),Id("f"),[]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test38(self):
        input = """class a {}
        class b extends a {}
        class c extends b{}
        class d extends c{}
        """
        expect = str(Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[],Id("a")),ClassDecl(Id("c"),[],Id("b")),ClassDecl(Id("d"),[],Id("c"))]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test39(self):
        input = """class Shape {
            void main() {
                int b = 4;
                boolean a = b > 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("b"),IntType(),
        IntLiteral(4)),VarDecl(Id("a"),BoolType(),BinaryOp(">",Id("b"),IntLiteral(5)))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test40(self):
        input = """class Shape {
            void main() {
                int[10] a;
                int i;
                for i := 0 to 9 do a[i] := i;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(10,IntType())),
        VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(0),IntLiteral(9),True,Assign(ArrayCell(Id("a"),Id("i")),Id("i")))]))])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test41(self):
        input = """class Shape {
            void main() {
                int[10] a = {1,2,3,4,5,6,7,8,9,10};
                int i;
                for i := 0 to 9 do a[i] := a[i] * i;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ArrayType(10,
        IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),
        IntLiteral(8),IntLiteral(9),IntLiteral(10)])),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(0),IntLiteral(9),True,
        Assign(ArrayCell(Id("a"),Id("i")),BinaryOp("*",ArrayCell(Id("a"),Id("i")),Id("i"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test42(self):
        input = """class Shape {
            void main() {
                int i;
                for i := 0 to 9 do break;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType())],
        [For(Id("i"),IntLiteral(0),IntLiteral(9),True,Break())]))])]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test43(self):
        input = """class Shape {
            void main() {
                int i;
                for i := 0 to 9 do continue;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType())],
        [For(Id("i"),IntLiteral(0),IntLiteral(9),True,Continue())]))])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test44(self):
        input = """class Shape {
            static int a;
            void main() {
                final int b = this.a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),MethodDecl(Static(),Id("main"),
        [],VoidType(),Block([ConstDecl(Id("b"),IntType(),FieldAccess(SelfLiteral(),Id("a")))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test45(self):
        input = """class Shape {
            static int a(int b) {
                return b * 2;
            }
            void main() {
                final int b = this.a(6);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("a"),[VarDecl(Id("b"),IntType())],IntType(),Block([],
        [Return(BinaryOp("*",Id("b"),IntLiteral(2)))])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([ConstDecl(Id("b"),IntType(),
        CallExpr(SelfLiteral(),Id("a"),[IntLiteral(6)]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test46(self):
        input = """class Shape {
            static int a(int b) {
                return b * 2;
            }
            final int b = 13;
            void main() {
                final int b = this.a(this.b);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("a"),[VarDecl(Id("b"),IntType())],IntType(),Block([],
        [Return(BinaryOp("*",Id("b"),IntLiteral(2)))])),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(13))),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([ConstDecl(Id("b"),IntType(),CallExpr(SelfLiteral(),Id("a"),
        [FieldAccess(SelfLiteral(),Id("b"))]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test47(self):
        input = """class Shape {
            void main() {
                float a = 34.23 + 3e4 - 23e-56 * 54e+96;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),
        FloatType(),BinaryOp("-",BinaryOp("+",FloatLiteral(34.23),FloatLiteral(3e4)),BinaryOp("*",FloatLiteral(23e-56),
        FloatLiteral(54e+96))))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test48(self):
        input = """class Shape {
            void main() {
                if !(32*87)==1234 then {}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[If(BinaryOp("==",
        UnaryOp("!",BinaryOp("*",IntLiteral(32),IntLiteral(87))),IntLiteral(1234)),Block([],[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test49(self):
        input = """class Shape {
            boolean b;
            void main() {
                if !(32*87)==1234 then {
                    this.b := true;
                }
                else this.b := false;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("b"),BoolType())),MethodDecl(Static(),
        Id("main"),[],VoidType(),Block([],[If(BinaryOp("==",UnaryOp("!",BinaryOp("*",IntLiteral(32),IntLiteral(87))),IntLiteral(1234)),
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("b")),BooleanLiteral(True))]),Assign(FieldAccess(SelfLiteral(),Id("b")),
        BooleanLiteral(False)))]))])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test50(self):
        input = """class Shape {
            void main() {
                if !(32*87)==1234 then 
                    io.writeIntLn(45*67);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[If(BinaryOp("==",
        UnaryOp("!",BinaryOp("*",IntLiteral(32),IntLiteral(87))),IntLiteral(1234)),CallStmt(Id("io"),Id("writeIntLn"),[BinaryOp("*",
        IntLiteral(45),IntLiteral(67))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test51(self):
        input = """class Shape {
            string a;
            static int b;
            final float c = 4.0;
            static final int[3] d = {1,2,3};
            final static boolean e = true;
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),StringType())),AttributeDecl(Static(),
        VarDecl(Id("b"),IntType())),AttributeDecl(Instance(),ConstDecl(Id("c"),FloatType(),FloatLiteral(4.0))),AttributeDecl(Static(),
        ConstDecl(Id("d"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),AttributeDecl(Static(),
        ConstDecl(Id("e"),BoolType(),BooleanLiteral(True)))])]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test52(self):
        input = """class Shape {
            boolean func(boolean a,b) {
                return a && b;
            }
            void main() {
                boolean b = this.func(5 > 6, 9 < 2);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),BoolType()),VarDecl(Id("b"),
        BoolType())],BoolType(),Block([],[Return(BinaryOp("&&",Id("a"),Id("b")))])),MethodDecl(Static(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("b"),BoolType(),CallExpr(SelfLiteral(),Id("func"),[BinaryOp(">",IntLiteral(5),IntLiteral(6)),
        BinaryOp("<",IntLiteral(9),IntLiteral(2))]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test53(self):
        input = """class Shape {
            void main() {
                int s = 0, i;
                for i := 1 to 100 do {
                    s := s + i;
                    if s > i * (s / 2) then break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),IntType(),
        IntLiteral(0)),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Assign(Id("s"),BinaryOp("+",
        Id("s"),Id("i"))),If(BinaryOp(">",Id("s"),BinaryOp("*",Id("i"),BinaryOp("/",Id("s"),IntLiteral(2)))),Break())]))]))])]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test54(self):
        input = """class Shape {
            void main() {
                int a;
                float b;
                string c;
                boolean d;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType()),
        VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),StringType()),VarDecl(Id("d"),BoolType())],[]))])]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test55(self):
        input = """class Shape {
            void main() {
                int a = 93, b = 435;
                float c = a / b;
                c := c * (a + b);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        IntLiteral(93)),VarDecl(Id("b"),IntType(),IntLiteral(435)),VarDecl(Id("c"),FloatType(),BinaryOp("/",Id("a"),Id("b")))],
        [Assign(Id("c"),BinaryOp("*",Id("c"),BinaryOp("+",Id("a"),Id("b"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test56(self):
        input = """class Shape {
            void main() {
                int a = 93;
                int i;
                for i := 1 to 100 do
                    a := a / 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        IntLiteral(93)),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Assign(Id("a"),BinaryOp("/",
        Id("a"),IntLiteral(2))))]))])]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test57(self):
        input = """class Shape {
            void main() {
                int a = 93;
                int i;
                for i := 1 to 100 do {
                    a := a / 2;
                    if a == 20 then continue;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        IntLiteral(93)),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Assign(Id("a"),
        BinaryOp("/",Id("a"),IntLiteral(2))),If(BinaryOp("==",Id("a"),IntLiteral(20)),Continue())]))]))])]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test58(self):
        input = """class Shape {
            void main() {
                int a = 93;
                int i;
                for i := 1 to 100 do {
                    a := a / 2;
                    if a == 20 then continue;
                    else if a < 10 then break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        IntLiteral(93)),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Assign(Id("a"),BinaryOp("/",
        Id("a"),IntLiteral(2))),If(BinaryOp("==",Id("a"),IntLiteral(20)),Continue(),If(BinaryOp("<",Id("a"),IntLiteral(10)),Break()))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test59(self):
        input = """class Shape {
            void main() {
                int a = 93, s = 0;
                int i;
                for i := 1 to 100 do {
                    a := a / 2;
                    if a == 20 then continue;
                    else if a < 10 then break;
                    s := s + a;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),IntType(),
        IntLiteral(93)),VarDecl(Id("s"),IntType(),IntLiteral(0)),VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(1),IntLiteral(100),
        True,Block([],[Assign(Id("a"),BinaryOp("/",Id("a"),IntLiteral(2))),If(BinaryOp("==",Id("a"),IntLiteral(20)),Continue(),
        If(BinaryOp("<",Id("a"),IntLiteral(10)),Break())),Assign(Id("s"),BinaryOp("+",Id("s"),Id("a")))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test60(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)))]))])]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test61(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
                else if i == 2 then a := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),
        If(BinaryOp("==",Id("i"),IntLiteral(2)),Assign(Id("a"),IntLiteral(2))))]))])]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test62(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
                else if i == 2 then a := 2;
                else if i == 3 then a := 3;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),If(BinaryOp("==",
        Id("i"),IntLiteral(2)),Assign(Id("a"),IntLiteral(2)),If(BinaryOp("==",Id("i"),IntLiteral(3)),Assign(Id("a"),IntLiteral(3)))))]))])]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test63(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
                else if i == 2 then a := 2;
                else if i == 3 then a := 3;
                else if i == 4 then a := 4;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),
        If(BinaryOp("==",Id("i"),IntLiteral(2)),Assign(Id("a"),IntLiteral(2)),If(BinaryOp("==",Id("i"),IntLiteral(3)),Assign(Id("a"),
        IntLiteral(3)),If(BinaryOp("==",Id("i"),IntLiteral(4)),Assign(Id("a"),IntLiteral(4))))))]))])]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test64(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
                else if i == 2 then a := 2;
                else if i == 3 then a := 3;
                else if i == 4 then a := 4;
                else if i == 5 then a := 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),If(BinaryOp("==",
        Id("i"),IntLiteral(2)),Assign(Id("a"),IntLiteral(2)),If(BinaryOp("==",Id("i"),IntLiteral(3)),Assign(Id("a"),IntLiteral(3)),
        If(BinaryOp("==",Id("i"),IntLiteral(4)),Assign(Id("a"),IntLiteral(4)),If(BinaryOp("==",Id("i"),IntLiteral(5)),Assign(Id("a"),
        IntLiteral(5)))))))]))])]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test65(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
                else if i == 2 then a := 2;
                else if i == 3 then a := 3;
                else if i == 4 then a := 4;
                else if i == 5 then a := 5;
                else if i == 6 then a := 6;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),If(BinaryOp("==",
        Id("i"),IntLiteral(2)),Assign(Id("a"),IntLiteral(2)),If(BinaryOp("==",Id("i"),IntLiteral(3)),Assign(Id("a"),IntLiteral(3)),
        If(BinaryOp("==",Id("i"),IntLiteral(4)),Assign(Id("a"),IntLiteral(4)),If(BinaryOp("==",Id("i"),IntLiteral(5)),Assign(Id("a"),
        IntLiteral(5)),If(BinaryOp("==",Id("i"),IntLiteral(6)),Assign(Id("a"),IntLiteral(6))))))))]))])]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test66(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
                else if i == 2 then a := 2;
                else if i == 3 then a := 3;
                else if i == 4 then a := 4;
                else if i == 5 then a := 5;
                else if i == 6 then a := 6;
                else if i == 7 then a := 7;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),
        If(BinaryOp("==",Id("i"),IntLiteral(2)),Assign(Id("a"),IntLiteral(2)),If(BinaryOp("==",Id("i"),IntLiteral(3)),Assign(Id("a"),
        IntLiteral(3)),If(BinaryOp("==",Id("i"),IntLiteral(4)),Assign(Id("a"),IntLiteral(4)),If(BinaryOp("==",Id("i"),IntLiteral(5)),
        Assign(Id("a"),IntLiteral(5)),If(BinaryOp("==",Id("i"),IntLiteral(6)),Assign(Id("a"),IntLiteral(6)),If(BinaryOp("==",Id("i"),
        IntLiteral(7)),Assign(Id("a"),IntLiteral(7)))))))))]))])]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test67(self):
        input = """class Shape {
            void main() {
                int i = 0;
                int a;
                if i == 1 then a := 1;
                else if i == 2 then a := 2;
                else if i == 3 then a := 3;
                else if i == 4 then a := 4;
                else if i == 5 then a := 5;
                else if i == 6 then a := 6;
                else if i == 7 then a := 7;
                else a := 0;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(0)),VarDecl(Id("a"),IntType())],[If(BinaryOp("==",Id("i"),IntLiteral(1)),Assign(Id("a"),IntLiteral(1)),
        If(BinaryOp("==",Id("i"),IntLiteral(2)),Assign(Id("a"),IntLiteral(2)),If(BinaryOp("==",Id("i"),IntLiteral(3)),Assign(Id("a"),
        IntLiteral(3)),If(BinaryOp("==",Id("i"),IntLiteral(4)),Assign(Id("a"),IntLiteral(4)),If(BinaryOp("==",Id("i"),IntLiteral(5)),
        Assign(Id("a"),IntLiteral(5)),If(BinaryOp("==",Id("i"),IntLiteral(6)),Assign(Id("a"),IntLiteral(6)),If(BinaryOp("==",Id("i"),
        IntLiteral(7)),Assign(Id("a"),IntLiteral(7)),Assign(Id("a"),IntLiteral(0)))))))))]))])]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test68(self):
        input = """class Shape {
            int f1() {
                return 1;
            }
            void main() {
                int i = this.f1();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[],IntType(),Block([],[Return(IntLiteral(1))])),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),CallExpr(SelfLiteral(),Id("f1"),[]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test69(self):
        input = """class Shape {
            int f1() {
                return 1;
            }
            int f2(int i) {
                return i * i;
            }
            void main() {
                int i = this.f2(this.f1());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[],IntType(),Block([],[Return(IntLiteral(1))])),
        MethodDecl(Instance(),Id("f2"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[Return(BinaryOp("*",Id("i"),Id("i")))])),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),CallExpr(SelfLiteral(),Id("f2"),
        [CallExpr(SelfLiteral(),Id("f1"),[])]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test70(self):
        input = """class Shape {
            int f1() {
                return 1;
            }
            int f2(int i) {
                return i * i;
            }
            int f3(int i) {
                return i * i * i;
            }
            void main() {
                int i = this.f3(this.f2(this.f1()));
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[],IntType(),Block([],[Return(IntLiteral(1))])),
        MethodDecl(Instance(),Id("f2"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[Return(BinaryOp("*",Id("i"),Id("i")))])),
        MethodDecl(Instance(),Id("f3"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[Return(BinaryOp("*",BinaryOp("*",Id("i"),Id("i")),
        Id("i")))])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),CallExpr(SelfLiteral(),Id("f3"),
        [CallExpr(SelfLiteral(),Id("f2"),[CallExpr(SelfLiteral(),Id("f1"),[])])]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test71(self):
        input = """class Shape {
            int f1() {
                return 1;
            }
            int f2(int i) {
                return i * i;
            }
            int f3(int i) {
                return i * i * i;
            }
            int f4(int i) {
                return i * i * i * i;
            }
            void main() {
                int i = this.f4(this.f3(this.f2(this.f1())));
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[],IntType(),Block([],[Return(IntLiteral(1))])),
        MethodDecl(Instance(),Id("f2"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[Return(BinaryOp("*",Id("i"),Id("i")))])),
        MethodDecl(Instance(),Id("f3"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[Return(BinaryOp("*",BinaryOp("*",Id("i"),Id("i")),
        Id("i")))])),MethodDecl(Instance(),Id("f4"),[VarDecl(Id("i"),IntType())],IntType(),Block([],[Return(BinaryOp("*",BinaryOp("*",
        BinaryOp("*",Id("i"),Id("i")),Id("i")),Id("i")))])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),
        IntType(),CallExpr(SelfLiteral(),Id("f4"),[CallExpr(SelfLiteral(),Id("f3"),[CallExpr(SelfLiteral(),Id("f2"),
        [CallExpr(SelfLiteral(),Id("f1"),[])])])]))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test72(self):
        input = """class Shape {
            int f1() {
                return 1;
            }
            void main() {
                int i = 4;
                i := i * this.f1();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[],IntType(),Block([],[Return(IntLiteral(1))])),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(4))],[Assign(Id("i"),BinaryOp("*",
        Id("i"),CallExpr(SelfLiteral(),Id("f1"),[])))]))])]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test73(self):
        input = """class Shape {
            int f1() {
                return 1;
            }
            int f2() {
                return 2;
            }
            void main() {
                int i = this.f1() * this.f2();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[],IntType(),Block([],[Return(IntLiteral(1))])),
        MethodDecl(Instance(),Id("f2"),[],IntType(),Block([],[Return(IntLiteral(2))])),MethodDecl(Static(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("i"),IntType(),BinaryOp("*",CallExpr(SelfLiteral(),Id("f1"),[]),CallExpr(SelfLiteral(),Id("f2"),[])))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test74(self):
        input = """class Shape {
            int f1(int i) {
                return i * 2;
            }
            /*int f2(int i) {
                return i * 3;
            }*/
            void main() {
                int i = 1;
                i := i * this.f1(i);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[VarDecl(Id("i"),IntType())],IntType(),Block([],
        [Return(BinaryOp("*",Id("i"),IntLiteral(2)))])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(1))],[Assign(Id("i"),BinaryOp("*",Id("i"),CallExpr(SelfLiteral(),Id("f1"),[Id("i")])))]))])]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test75(self):
        input = """class Shape {
            int f1(int i) {
                return i * 2;
            }
            int f2(int i) {
                return i * 3;
            }
            void main() {
                int i = 1;
                i := this.f2(i) * this.f1(i);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[VarDecl(Id("i"),IntType())],IntType(),Block([],
        [Return(BinaryOp("*",Id("i"),IntLiteral(2)))])),MethodDecl(Instance(),Id("f2"),[VarDecl(Id("i"),IntType())],IntType(),Block([],
        [Return(BinaryOp("*",Id("i"),IntLiteral(3)))])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),
        IntLiteral(1))],[Assign(Id("i"),BinaryOp("*",CallExpr(SelfLiteral(),Id("f2"),[Id("i")]),CallExpr(SelfLiteral(),Id("f1"),[Id("i")])))]))])]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test76(self):
        input = """class Shape {
            int f1(int i) {
                return i * 2;
            }
            int f2(int i) {
                return i * 3;
            }
        }
        class con extends Shape {
            void main() {
                int i = 1;
                Shape b = new Shape();
                i := b.f2(i) * b.f1(i);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("f1"),[VarDecl(Id("i"),IntType())],IntType(),Block([],
        [Return(BinaryOp("*",Id("i"),IntLiteral(2)))])),MethodDecl(Instance(),Id("f2"),[VarDecl(Id("i"),IntType())],IntType(),Block([],
        [Return(BinaryOp("*",Id("i"),IntLiteral(3)))]))]),ClassDecl(Id("con"),[MethodDecl(Static(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("i"),IntType(),IntLiteral(1)),VarDecl(Id("b"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[]))],
        [Assign(Id("i"),BinaryOp("*",CallExpr(Id("b"),Id("f2"),[Id("i")]),CallExpr(Id("b"),Id("f1"),[Id("i")])))]))],Id("Shape"))]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test77(self):
        input = """class Shape {
            int a, b;
            Shape(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i = 1;
                Shape b = new Shape(4, 5);
                i := b.a * b.b;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))]))]),
        ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType(),IntLiteral(1)),
        VarDecl(Id("b"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[IntLiteral(4),IntLiteral(5)]))],[Assign(Id("i"),BinaryOp("*",
        FieldAccess(Id("b"),Id("a")),FieldAccess(Id("b"),Id("b"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test78(self):
        input = """class Shape {
            int a, b;
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                con b = new con();
                b.gan(3, 4);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType()))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),
        IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Assign(FieldAccess(SelfLiteral(),Id("b")),
        Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("b"),
        ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),Id("gan"),[IntLiteral(3),IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test79(self):
        input = """class Shape {
            int a, b;
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i;
                con b = new con();
                b.gan(3, 4);
                i := b.a + b.b;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType()))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),
        IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Assign(FieldAccess(SelfLiteral(),Id("b")),
        Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType()),
        VarDecl(Id("b"),ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),Id("gan"),[IntLiteral(3),IntLiteral(4)]),
        Assign(Id("i"),BinaryOp("+",FieldAccess(Id("b"),Id("a")),FieldAccess(Id("b"),Id("b"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test80(self):
        input = """class Shape {
            int a, b;
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                con b = new con();
                b.gan(3, 4);
                b.a := 6;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType()))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),
        IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Assign(FieldAccess(SelfLiteral(),Id("b")),
        Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("b"),
        ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),Id("gan"),[IntLiteral(3),IntLiteral(4)]),Assign(FieldAccess(Id("b"),
        Id("a")),IntLiteral(6))]))])]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test81(self):
        input = """class Shape {
            int a, b;
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                con b = new con();
                b.gan(3, 4);
                b.a := b.b * b.a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType()))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),
        IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Assign(FieldAccess(SelfLiteral(),Id("b")),
        Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("b"),
        ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),Id("gan"),[IntLiteral(3),IntLiteral(4)]),
        Assign(FieldAccess(Id("b"),Id("a")),BinaryOp("*",FieldAccess(Id("b"),Id("b")),FieldAccess(Id("b"),Id("a"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test82(self):
        input = """class Shape {
            int a, b;
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                con b = new con();
                b.gan(3, 4);
                b.a := b.b * b.a - b.b / b.a * b.b + b.b;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType()))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),
        IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Assign(FieldAccess(SelfLiteral(),Id("b")),
        Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("b"),
        ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),Id("gan"),[IntLiteral(3),IntLiteral(4)]),
        Assign(FieldAccess(Id("b"),Id("a")),BinaryOp("+",BinaryOp("-",BinaryOp("*",FieldAccess(Id("b"),Id("b")),FieldAccess(Id("b"),
        Id("a"))),BinaryOp("*",BinaryOp("/",FieldAccess(Id("b"),Id("b")),FieldAccess(Id("b"),Id("a"))),FieldAccess(Id("b"),Id("b")))),
        FieldAccess(Id("b"),Id("b"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test83(self):
        input = """class Shape {
            int a, b;
            int geta() {
                return a;
            }
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i;
                con b = new con();
                b.gan(3, 4);
                i := b.geta();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("geta"),[],IntType(),Block([],[Return(Id("a"))]))]),ClassDecl(Id("con"),
        [MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([],
        [Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))]))],Id("Shape")),
        ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("b"),
        ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),Id("gan"),[IntLiteral(3),IntLiteral(4)]),Assign(Id("i"),
        CallExpr(Id("b"),Id("geta"),[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test84(self):
        input = """class Shape {
            int a, b;
            int[2] get() {
                int[2] x;
                x[0] := this.a;
                x[1] := this.b;
                return x;
            }
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i;
                con b = new con();
                b.gan(3, 4);
                i := b.get()[0];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("get"),[],ArrayType(2,IntType()),Block([VarDecl(Id("x"),ArrayType(2,
        IntType()))],[Assign(ArrayCell(Id("x"),IntLiteral(0)),FieldAccess(SelfLiteral(),Id("a"))),Assign(ArrayCell(Id("x"),IntLiteral(1)),
        FieldAccess(SelfLiteral(),Id("b"))),Return(Id("x"))]))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),
        IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),
        Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],
        VoidType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("b"),ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),
        Id("gan"),[IntLiteral(3),IntLiteral(4)]),Assign(Id("i"),ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(0)))]))])]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test85(self):
        input = """class Shape {
            int a, b;
            int[2] get() {
                int[2] x;
                x[0] := this.a;
                x[1] := this.b;
                return x;
            }
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i;
                con b = new con();
                b.gan(3, 4);
                i := b.get()[0] * b.get()[1];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("get"),[],ArrayType(2,IntType()),Block([VarDecl(Id("x"),ArrayType(2,
        IntType()))],[Assign(ArrayCell(Id("x"),IntLiteral(0)),FieldAccess(SelfLiteral(),Id("a"))),Assign(ArrayCell(Id("x"),IntLiteral(1)),
        FieldAccess(SelfLiteral(),Id("b"))),Return(Id("x"))]))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),
        IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),
        Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],
        VoidType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("b"),ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),
        Id("gan"),[IntLiteral(3),IntLiteral(4)]),Assign(Id("i"),BinaryOp("*",ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(0)),
        ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(1))))]))])]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test86(self):
        input = """class Shape {
            int a, b;
            int[2] get() {
                int[2] x;
                x[0] := this.a;
                x[1] := this.b;
                return x;
            }
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i;
                con b = new con();
                b.gan(3, 4);
                if b.get()[0] > b.get()[1] then i := b.get()[0];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("get"),[],ArrayType(2,IntType()),Block([VarDecl(Id("x"),ArrayType(2,
        IntType()))],[Assign(ArrayCell(Id("x"),IntLiteral(0)),FieldAccess(SelfLiteral(),Id("a"))),Assign(ArrayCell(Id("x"),IntLiteral(1)),
        FieldAccess(SelfLiteral(),Id("b"))),Return(Id("x"))]))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),
        IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),
        Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],
        VoidType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("b"),ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),
        Id("gan"),[IntLiteral(3),IntLiteral(4)]),If(BinaryOp(">",ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(0)),
        ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(1))),Assign(Id("i"),ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(0))))]))])]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test87(self):
        input = """class Shape {
            int a, b;
            int[2] get() {
                int[2] x;
                x[0] := this.a;
                x[1] := this.b;
                return x;
            }
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i;
                con b = new con();
                b.gan(3, 4);
                if b.get()[0] > b.get()[1] then i := b.get()[0];
                else i := b.get()[1];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("get"),[],ArrayType(2,IntType()),Block([VarDecl(Id("x"),ArrayType(2,
        IntType()))],[Assign(ArrayCell(Id("x"),IntLiteral(0)),FieldAccess(SelfLiteral(),Id("a"))),Assign(ArrayCell(Id("x"),IntLiteral(1)),
        FieldAccess(SelfLiteral(),Id("b"))),Return(Id("x"))]))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),[VarDecl(Id("a"),
        IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),
        Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],
        VoidType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("b"),ClassType(Id("con")),NewExpr(Id("con"),[]))],[CallStmt(Id("b"),
        Id("gan"),[IntLiteral(3),IntLiteral(4)]),If(BinaryOp(">",ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(0)),
        ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(1))),Assign(Id("i"),ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(0))),
        Assign(Id("i"),ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(1))))]))])]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test88(self):
        input = """class Shape {
            int a, b;
            int[2] get() {
                int[2] x;
                x[0] := this.a;
                x[1] := this.b;
                return x;
            }
        }
        class con extends Shape {
            void gan(int a, b) {
                this.a := a;
                this.b := b;
            }
        }
        class man{
            void main() {
                int i, s = 0;
                con b = new con();
                b.gan(1, 4);
                for i := b.get()[1] downto b.get()[0] do
                    s := s + i; 
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),IntType())),MethodDecl(Instance(),Id("get"),[],ArrayType(2,IntType()),Block([VarDecl(Id("x"),ArrayType(2,
        IntType()))],[Assign(ArrayCell(Id("x"),IntLiteral(0)),FieldAccess(SelfLiteral(),Id("a"))),Assign(ArrayCell(Id("x"),
        IntLiteral(1)),FieldAccess(SelfLiteral(),Id("b"))),Return(Id("x"))]))]),ClassDecl(Id("con"),[MethodDecl(Instance(),Id("gan"),
        [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),
        Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))]))],Id("Shape")),ClassDecl(Id("man"),[MethodDecl(Static(),Id("main"),[],
        VoidType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("s"),IntType(),IntLiteral(0)),VarDecl(Id("b"),ClassType(Id("con")),
        NewExpr(Id("con"),[]))],[CallStmt(Id("b"),Id("gan"),[IntLiteral(1),IntLiteral(4)]),For(Id("i"),ArrayCell(CallExpr(Id("b"),
        Id("get"),[]),IntLiteral(1)),ArrayCell(CallExpr(Id("b"),Id("get"),[]),IntLiteral(0)),False,Assign(Id("s"),BinaryOp("+",
        Id("s"),Id("i"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test89(self):
        input = """class Shape {
            void main() {
                int i;
                for i:= 1 to 100 do
                    i := i + i;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType())],
        [For(Id("i"),IntLiteral(1),IntLiteral(100),True,Assign(Id("i"),BinaryOp("+",Id("i"),Id("i"))))]))])]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test90(self):
        input = """class Shape {
            void main() {
                int i;
                for i:= 1 to 100 do {
                    i := i + i;
                    if (i == 25) then break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType())],
        [For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Assign(Id("i"),BinaryOp("+",Id("i"),Id("i"))),If(BinaryOp("==",
        Id("i"),IntLiteral(25)),Break())]))]))])]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test91(self):
        input = """class Shape {
            void main() {
                int i;
                for i:= 1 to 100 do {
                    i := i + i;
                    if (i == 25) then {break;}
                    else {continue;}
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType())],
        [For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Assign(Id("i"),BinaryOp("+",Id("i"),Id("i"))),If(BinaryOp("==",Id("i"),
        IntLiteral(25)),Block([],[Break()]),Block([],[Continue()]))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test92(self):
        input = """class Shape {
            void main() {
                int i;
                for i:= 1 to 100 do {
                    i := i + i;
                    if (i == 25) then i := 50;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType())],
        [For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Assign(Id("i"),BinaryOp("+",Id("i"),Id("i"))),If(BinaryOp("==",Id("i"),
        IntLiteral(25)),Assign(Id("i"),IntLiteral(50)))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test93(self):
        input = """class Shape {
            void main() {
                int i;
                for i:= 1 to 100 do {
                    i := i + i;
                    if (i == 25) then i := 50;
                    else i := 500;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType())],
        [For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Assign(Id("i"),BinaryOp("+",Id("i"),Id("i"))),If(BinaryOp("==",Id("i"),
        IntLiteral(25)),Assign(Id("i"),IntLiteral(50)),Assign(Id("i"),IntLiteral(500)))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test94(self):
        input = """class Shape {
            static final int o = 3;
            void main() {
                int o = 5;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Static(),ConstDecl(Id("o"),IntType(),IntLiteral(3))),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("o"),IntType(),IntLiteral(5))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test95(self):
        input = """class Shape {
            static final int o = 3;
            void main() {
                int o = this.o;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Static(),ConstDecl(Id("o"),IntType(),IntLiteral(3))),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("o"),IntType(),FieldAccess(SelfLiteral(),Id("o")))],[]))])]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test96(self):
        input = """class Shape {
            static final int o = 3;
            void main() {
                float a;
                a := this.o * 34.2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Static(),ConstDecl(Id("o"),IntType(),IntLiteral(3))),
        MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),FloatType())],[Assign(Id("a"),BinaryOp("*",
        FieldAccess(SelfLiteral(),Id("o")),FloatLiteral(34.2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test97(self):
        input = """class Shape {
            float a, b;
            Shape(int c, d) {
                this.a := c * d;
                this.b := c / d;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),FloatType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),FloatType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),BinaryOp("*",Id("c"),Id("d"))),Assign(FieldAccess(SelfLiteral(),Id("b")),
        BinaryOp("/",Id("c"),Id("d")))]))])]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test98(self):
        input = """class Shape {
            float a, b;
            Shape(int c, d) {
                this.a := c * d;
                this.b := c / d;
            }
            final static float pi = 3.14;
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("a"),FloatType())),AttributeDecl(Instance(),
        VarDecl(Id("b"),FloatType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],None,
        Block([],[Assign(FieldAccess(SelfLiteral(),Id("a")),BinaryOp("*",Id("c"),Id("d"))),Assign(FieldAccess(SelfLiteral(),Id("b")),
        BinaryOp("/",Id("c"),Id("d")))])),AttributeDecl(Static(),ConstDecl(Id("pi"),FloatType(),FloatLiteral(3.14)))])]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test99(self):
        input = """class Example1 {
            int factorial(int n){
                if n == 0 then return 1; else return n * this.factorial(n - 1);
            }
            void main(){
                int x;
                x := io.readInt();
                io.writeIntLn(this.factorial(x));
            }
        }"""
        expect = str(Program([ClassDecl(Id("Example1"),[MethodDecl(Instance(),Id("factorial"),[VarDecl(Id("n"),IntType())],IntType(),
        Block([],[If(BinaryOp("==",Id("n"),IntLiteral(0)),Return(IntLiteral(1)),Return(BinaryOp("*",Id("n"),CallExpr(SelfLiteral(),
        Id("factorial"),[BinaryOp("-",Id("n"),IntLiteral(1))]))))])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("x"),
        IntType())],[Assign(Id("x"),CallExpr(Id("io"),Id("readInt"),[])),CallStmt(Id("io"),Id("writeIntLn"),[CallExpr(SelfLiteral(),
        Id("factorial"),[Id("x")])])]))])]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test100(self):
        input = """class Shape {
            float length,width;
            float getArea() {}
            Shape(float length,width){
                this.length := length;
                this.width := width;
            }
        }
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width;
            }
        }
        class Triangle extends Shape {
            float getArea(){
                return this.length*this.width / 2;
            }
        }
        class Example2 {
            void main(){
                Shape s;
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),
        VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),
        Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),
        Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),
        [MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),
        FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],
        FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),
        Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),
        Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[Assign(Id("s"),NewExpr(Id("Rectangle"),[IntLiteral(3),IntLiteral(4)])),
        CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("s"),Id("getArea"),[])]),Assign(Id("s"),NewExpr(Id("Triangle"),[IntLiteral(3),
        IntLiteral(4)])),CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("s"),Id("getArea"),[])])]))])]))
        self.assertTrue(TestAST.test(input,expect,399))