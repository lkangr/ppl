import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
        
    def test2(self): 
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test3(self):
        input = """class { }"""
        expect = "Error on line 1 col 6: {"
        self.assertTrue(TestParser.test(input, expect, 202))
        
    def test4(self):
        input = """class ABC }"""
        expect = "Error on line 1 col 10: }"
        self.assertTrue(TestParser.test(input, expect, 203))
        
    def test5(self):
        input = """class ABC extends DEF { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        
    def test6(self):
        input = """class ABC {"""
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 205))
        
    def test7(self):
        input = """class ABC {
                     static final int numOfShape = 0;
                     final int immuAttribute = 0;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
        
    def test8(self):
        input = """class ABC {
                     final static int numOfShape = 0;
                     float length,width;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
        
    def test9(self):
        input = """class ABC {
                     final static int numOfShape  = 4, imm;
                     float length,width = 5;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        
    def test10(self):
        input = """class ABC {
                     final static numOfShape;
                     float length,width = 5;
                   }"""
        expect = "Error on line 2 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 209))
        
    def test11(self):
        input = """class ABC {
                     static int numOfShape() {}
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
        
    def test12(self):
        input = """class ABC {
                     static final int numOfShape() {}
                   }"""
        expect = "Error on line 2 col 48: ("
        self.assertTrue(TestParser.test(input, expect, 211))
        
    def test13(self):
        input = """class ABC {
                     static numOfShape() {}
                   }"""
        expect = "Error on line 2 col 38: ("
        self.assertTrue(TestParser.test(input, expect, 212))

    def test14(self):
        input = """class ABC {
                     static int numOfShape();
                   }"""
        expect = "Error on line 2 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test15(self):
        input = """class ABC {
                     float numOfShape()
                   }"""
        expect = "Error on line 3 col 19: }"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test16(self):
        input = """class Rectangle extends Shape {
                     float getArea(){
                       return this.length*this.width;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test17(self):
        input = """class Shape {
                     float length,width;
                     Shape(float length,width){
                       this.length := length;
                       this.width := width;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test18(self):
        input = """class Shape {
                     void setLength(int length) {
                       this.length := length;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test19(self):
        input = """class Shape {
                     void setLength(int length) {
                       this.length = length;
                     }
                   }"""
        expect = "Error on line 3 col 35: ="
        self.assertTrue(TestParser.test(input, expect, 218))

    def test20(self):
        input = """class Shape { # comment
                     int[5] a;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test21(self):
        input = """class Shape { # comment
                     int[5] a = {1, 2, 3, 4, 5};
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test22(self):
        input = """class Shape { # comment
                     int[5] a = {1, 2, 3.5, 4, 5};
                   }"""
        expect = "Error on line 2 col 39: 3.5"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test23(self):
        input = """class Shape { # comment
                     int[5] a = {1, 2 3, 4, 5};
                   }"""
        expect = "Error on line 2 col 38: 3"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test24(self):
        input = """class Shape { # comment
                     string str = "strstrstr\\n";
                     boolean b = true;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test25(self):
        input = """class Shape { # comment
                     string str = "strstrstr\\n"
                     boolean b = true;
                   }"""
        expect = "Error on line 3 col 21: boolean"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test26(self):
        input = """class Shape {
                     boolean b = 5 > 4;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test27(self):
        input = """class Shape {
                     int a;
                     void b(c) {
                       this.a := c*c*c;
                     }
                   }"""
        expect = "Error on line 3 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test28(self):
        input = """class Shape {
                     int a;
                     void b(int c) {
                       this.a := c*c*c;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test29(self):
        input = """class Shape {
                     int[6] a;
                     a[2] := 6;
                   }"""
        expect = "Error on line 3 col 26: :="
        self.assertTrue(TestParser.test(input, expect, 228))
    
    def test30(self):
        input = """class Shape {
                     int[6] a;
                     void func() {
                       a[2] := 6;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test31(self):
        input = """class Shape {
                     int[6] a;
                     void func(int[6] b) {
                       a[3+x.foo(2)] := a[b[2]] +3;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test32(self):
        input = """class Shape {
                     int[6] a;
                     void func(foo) {
                       a[3+x.foo(2)] := a[b[2]] +3;
                     }
                   }"""
        expect = "Error on line 3 col 34: )"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test33(self):
        input = """class Shape {
                     void func() {
                       x.b[2] := x.m()[3];
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test34(self):
        input = """class Shape {
                     void func() {
                       this.aPI := 3.14;
                       value := x.foo(5);
                       l[3] := value * 2;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test35(self):
        input = """class Shape {
                     int a;
                     a := 6;
                   }"""
        expect = "Error on line 3 col 23: :="
        self.assertTrue(TestParser.test(input, expect, 234))

    def test36(self):
        input = """class Shape {
                     int a := 5;
                   }"""
        expect = "Error on line 2 col 27: :="
        self.assertTrue(TestParser.test(input, expect, 235))

    def test37(self):
        input = """class Shape {
                     int a = 5;
                     void func(boolean d) {
                       a = 3;
                     }
                   }"""
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.test(input, expect, 236))

    def test38(self):
        input = """class Shape {
                     int a = 5;
                     void func(boolean d) {
                       a = 3;
                     }
                   }"""
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.test(input, expect, 237))

    def test39(self):
        input = """class a {}
                   class b {}
                   class c extends a {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test40(self):
        input = """class Shape {
                     int a = 5;
                     io.writeIntLn(a);
                   }"""
        expect = "Error on line 3 col 23: ."
        self.assertTrue(TestParser.test(input, expect, 239))

    def test41(self):
        input = """class Shape {
                     int a = 5;
                     void func() {
                       io.writeIntLn(a);
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test42(self):
        input = """class Shape {
                     string a;
                     string func() {
                       a := io.readStr();
                       return a;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test43(self):
        input = """class Shape {
                     float func(int a, float b) {
                       return a * b;
                     }
                   }"""
        expect = "Error on line 2 col 39: float"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test44(self):
        input = """class Shape {
                     float func(int a ,b; float b) {
                       return a + c * b;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test45(self):
        input = """class Shape {
                     float func(float b) {
                       float c = b / 2;
                       return c;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test46(self):
        input = """class Example1 {
                     void main(){
                       int x;
                       x := io.readInt();
                       io.writeIntLn(this.factorial(x));
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test47(self):
        input = """class Example1 {
                     int func(int a) {
                       return a * a;
                     }
                     void main(){
                       int x;
                       x := this.func(x);
                       io.writeIntLn(x);
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test48(self):
        input = """class Example1 {
                     int func(int a) {
                       return a * a;
                     }
                     void main(){
                       int x;
                       x := func(x);
                       io.writeIntLn(x);
                     }
                   }"""
        expect = "Error on line 7 col 32: ("
        self.assertTrue(TestParser.test(input, expect, 247))

    def test49(self):
        input = """class Example1 {
                     float func(float[5] f) {
                       f[2] := f[3];
                       return f[4];
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test50(self):
        input = """class Example1 {
                     float func(float[5] f) {
                       f[2] := f[3];
                       return f[4];
                       f[0];
                     }
                   }"""
        expect = "Error on line 5 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test51(self):
        input = """class Example1 {
                     if true then io.writeStrLn("Expression is true");
                   }"""
        expect = "Error on line 2 col 21: if"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test52(self):
        input = """class Example1 {
                     int a = 5;
                     void func(int b) {
                       if a == b then io.writeStrLn("Expression is true");
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test53(self):
        input = """class Example1 {
                     int a = 5;
                     void func(int b) {
                       if a == b then io.writeStrLn("Expression is true");
                       else io.writeStrLn("Expression is false");
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test54(self):
        input = """class Example1 {
                     int a = 5;
                     void func(int b) {
                       if a >= b return a;
                       else return b;
                     }
                   }"""
        expect = "Error on line 4 col 33: return"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test55(self):
        input = """class Example1 {
                     int a = 5;
                     void func(int b) {
                       if a >= b then return a;
                       else return b;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test56(self):
        input = """class Example1 {
                     int a = 5;
                     void func(int b) {
                       if a = b then return a;
                       else return b;
                     }
                   }"""
        expect = "Error on line 4 col 28: ="
        self.assertTrue(TestParser.test(input, expect, 255))

    def test57(self):
        input = """class Example1 {
                     int a = 5;
                     void func(int b) {
                       if a < b then a := b;
                       else b := a;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test58(self):
        input = """class Example1 {
                     int a = 5;
                     void func(int b) {
                       if a < b then a := b
                       else b := a;
                     }
                   }"""
        expect = "Error on line 5 col 23: else"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test59(self):
        input = """class Example1 {
                     void func(int b) {
                       if true then {} else {}
                   }"""
        expect = "Error on line 4 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test60(self):
        input = """class Example1 {
                     void func(int b) {
                       if true then {} else {}
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test61(self):
        input = """class Example1 {
                     void func(int b) {
                       if true then {}
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test62(self):
        input = """class Example1 {
                     void func(int b) {
                       int i;
                       for i := 1 to 100 do {}
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test63(self):
        input = """class Example1 {
                     int i;
                     for i := 1 to 100 do {}
                   }"""
        expect = "Error on line 3 col 21: for"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test64(self):
        input = """class Example1 {
                     void func(int b) {
                       int i;
                       for i := 1 to 100 do {
                         io.writeIntLn(i);
                         Intarray[i] := i * (i + 1);
                       }
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test65(self):
        input = """class Example1 {
                     void func(int b) {
                       int i;
                       for i := 1 to 100 {
                         io.writeIntLn(i);
                         Intarray[i] := i + 1;
                       }
                     }
                   }"""
        expect = "Error on line 4 col 41: {"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test66(self):
        input = """class Example1 {
                     void func(int b) {
                       int x;
                       for x := 5 downto 2 do {
                         io.writeIntLn(x);
                       }
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test67(self):
        input = """class Example1 {
                     void func(int b) {
                       int x;
                       for x := 5 downto 2 do io.writeIntLn(x);
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test68(self):
        input = """class Example1 {
                     void func(int b) {
                       for x := 5 downto 2 do {
                         for i := 2 to 5 do s := s + x * i;
                       }
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test69(self):
        input = """class Example1 {
                     void func(int b) {
                       for x := 5 downto 2 do {
                         if x == 3 then break;
                       }
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test70(self):
        input = """class Example1 {
                     void func(int b) {
                       for x := 5 downto 2 do
                         if x == 3 then break; else continue;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test71(self):
        input = """class Example1 {
                     void func(int b) {
                       for x := 1 to 100 do
                         if x == 6 then break;
                         if x == 9 then return x;
                         else continue;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test72(self):
        input = """class Example1 {
                     void func(int b) {
                       for x := 1 to 100 do
                         if x == 6 then break;
                         x := x + 2;
                         if x == 9 then return x;
                         continue;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test73(self):
        input = """class Example1 {
                     void func(int b) {
                       for x := 1 to 100 do
                         obj.func(x);
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test74(self):
        input = """class Example1 {
                     void func(int b) {
                       for x = 1 to 100 do
                         obj.func(x);
                     }
                   }"""
        expect = "Error on line 3 col 29: ="
        self.assertTrue(TestParser.test(input, expect, 273))

    def test75(self):
        input = """class Example1 {
                     void func(int b) {
                       for x := 1 to 100 do
                         int c = x;
                         return c;
                     }
                   }"""
        expect = "Error on line 4 col 25: int"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test76(self):
        input = """class Example1 {
                     void func(int b) {
                       int c;
                       for x := 1 to 100 do
                         c = x;
                         return c;
                     }
                   }"""
        expect = "Error on line 5 col 27: ="
        self.assertTrue(TestParser.test(input, expect, 275))

    def test77(self):
        input = """class Example1 {
                     void func(int b) {
                       int c;
                       for x := 1 to 100 do
                         c := x;
                         return c;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test78(self):
        input = """class Example1 {
                     void func(int b) {
                       break;
                       continue;
                       return;
                     }
                   }"""
        expect = "Error on line 5 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test79(self):
        input = """class Example1 {
                     void func(int b) {
                       break;
                       continue;
                       return a;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test80(self):
        input = """class Example1 {
                     void func(int b) {
                       if true then
                         if false then break;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test81(self):
        input = """class Example1 {
                     float a = 9;
                     void func(int b) {
                       if a == b then 
                         for i := 1 to 10 do
                           io.writeIntLn(i);
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test82(self):
        input = """class Example1 {
                     float a = 9;
                     void func(int b) {
                       if a == b else return a;
                   }"""
        expect = "Error on line 4 col 33: else"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test83(self):
        input = """class Example1 {
                     float a = 9;
                     void func(int b) {
                       if a == b then return a;
                     }}
                   }"""
        expect = "Error on line 6 col 19: }"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test84(self):
        input = """class Example1 {
                     for i := 1 to 10 do a[i] := i;
                   }"""
        expect = "Error on line 2 col 21: for"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test85(self):
        input = """class Example1 {
                     void func(int b[5]) {
                       for i := 0 to 5 do b[i] := i;
                     }
                   }"""
        expect = "Error on line 2 col 36: ["
        self.assertTrue(TestParser.test(input, expect, 284))

    def test86(self):
        input = """class Example1 {
                     void func(int[5] b) {
                       for i := 0 to 5 do b[i] := i;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test87(self):
        input = """class Example1 {
                     void func(int[5] b) {
                       for i := 0 to 5 do b[i] = i;
                     }
                   }"""
        expect = "Error on line 3 col 47: ="
        self.assertTrue(TestParser.test(input, expect, 286))

    def test88(self):
        input = """class Example1 {
                     break;
                   }"""
        expect = "Error on line 2 col 21: break"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test89(self):
        input = """class Example1 {
                     continue;
                   }"""
        expect = "Error on line 2 col 21: continue"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test90(self):
        input = """class Example1 {
                     int f1() {}
                     float f2() {}
                     string f3() {
                       this.f1();
                       this.f2();
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test91(self):
        input = """class Example1 {
                     class ex2 extends Example1 {}
                   }"""
        expect = "Error on line 2 col 21: class"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test92(self):
        input = """class Example1 {
                     {int a = 3;}
                   }"""
        expect = "Error on line 2 col 21: {"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test93(self):
        input = """class Example1 {
                     int a = 3, b = 4;
                     float c = a * b;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test94(self):
        input = """class Example1 {
                     int c = "sfkfkj";
                     string b(boolean a) {
                       return a;
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test95(self):
        input = """class Example1 {
                     void main() {
                       io.writeStrLn("Hello World!");
                     }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test96(self):
        input = """class Example1 {
                     void main() {
                       io.writeStrLn("Hello World!";
                     }
                   }"""
        expect = "Error on line 3 col 51: ;"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test97(self):
        input = """class Example1 {
                     void main {
                       io.writeStrLn("Hello World!");
                     }
                   }"""
        expect = "Error on line 2 col 31: {"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test98(self):
        input = """class Example1() {
                     void main() {
                       io.writeStrLn("Hello World!");
                     }
                   }"""
        expect = "Error on line 1 col 14: ("
        self.assertTrue(TestParser.test(input, expect, 297))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))