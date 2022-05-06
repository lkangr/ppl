import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        self.assertTrue(TestLexer.test("AKJDC","AKJDC,<EOF>",100))
    def test_2(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_3(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_4(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
    def test_5(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))
    def test_6(self):
        self.assertTrue(TestLexer.test("     ", "<EOF>", 105))
    def test_7(self):
        self.assertTrue(TestLexer.test(" \t\f\r\n", "<EOF>", 106))
    def test_8(self):
        self.assertTrue(TestLexer.test("sdj 123", "sdj,123,<EOF>", 107))
    def test_9(self):
        self.assertTrue(TestLexer.test("432.54\n9e+12", "432.54,9e+12,<EOF>", 108))
    def test_10(self):
        self.assertTrue(TestLexer.test("/*block comment*/", "<EOF>", 109))
    def test_11(self):
        self.assertTrue(TestLexer.test("/*other\nblock\ncomment*/", "<EOF>", 110))
    def test_12(self):
        self.assertTrue(TestLexer.test("12_dje98", "12,_dje98,<EOF>", 111))
    def test_13(self):
        self.assertTrue(TestLexer.test("_Identifer#line comment", "_Identifer,<EOF>", 112))
    def test_14(self):
        self.assertTrue(TestLexer.test("line1#line comment\nline2", "line1,line2,<EOF>", 113))
    def test_15(self):
        self.assertTrue(TestLexer.test("if then", "if,then,<EOF>", 114))
    def test_16(self):
        self.assertTrue(TestLexer.test("1+2", "1,+,2,<EOF>", 115))
    def test_17(self):
        self.assertTrue(TestLexer.test("x:=34/12", "x,:=,34,/,12,<EOF>", 116))
    def test_18(self):
        self.assertTrue(TestLexer.test("value := x.foo(5);", "value,:=,x,.,foo,(,5,),;,<EOF>", 117))
    def test_19(self):
        self.assertTrue(TestLexer.test("float a,b;", "float,a,,,b,;,<EOF>", 118))
    def test_20(self):
        self.assertTrue(TestLexer.test("l[3] := value * 2;", "l,[,3,],:=,value,*,2,;,<EOF>", 119))
    def test_21(self):
        self.assertTrue(TestLexer.test("float b := 0E-3", "float,b,:=,0E-3,<EOF>", 120))
    def test_22(self):
        self.assertTrue(TestLexer.test("\"this is a string\"", "\"this is a string\",<EOF>", 121))
    def test_23(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\"", "\"This is a string containing tab \\t\",<EOF>", 122))
    def test_24(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "\"He asked me: \\\"Where is John?\\\"\",<EOF>", 123))
    def test_25(self):
        self.assertTrue(TestLexer.test("\"hekdjs dsfkd", "Unclosed String: \"hekdjs dsfkd", 124))
    def test_26(self):
        self.assertTrue(TestLexer.test("\"line1\nline2\"", "Unclosed String: \"line1\n\n", 125))
    def test_27(self):
        self.assertTrue(TestLexer.test("\"string1\"\"string2\"", "\"string1\",\"string2\",<EOF>", 126))
    def test_28(self):
        self.assertTrue(TestLexer.test("\"shflkd\\kds\"", "Illegal Escape In String: \"shflkd\\k", 127))
    def test_29(self):
        self.assertTrue(TestLexer.test("\"shf\\tds", "Unclosed String: \"shf\\tds", 128))
    def test_30(self):
        self.assertTrue(TestLexer.test("string a := \"a string\\n\"", "string,a,:=,\"a string\\n\",<EOF>", 129))
    def test_31(self):
        self.assertTrue(TestLexer.test("39.5>39.4 ", "39.5,>,39.4,<EOF>", 130))
    def test_32(self):
        self.assertTrue(TestLexer.test("23 hkde 3.12e+43", "23,hkde,3.12e+43,<EOF>", 131))
    def test_33(self):
        self.assertTrue(TestLexer.test("3E-12ehd90es", "3E-12,ehd90es,<EOF>", 132))
    def test_34(self):
        self.assertTrue(TestLexer.test("34e.12", "34,e,.,12,<EOF>", 133))
    def test_35(self):
        self.assertTrue(TestLexer.test("hdk$edl", "hdk,Error Token $", 134))
    def test_36(self):
        self.assertTrue(TestLexer.test("{1, 2, 3}", "{,1,,,2,,,3,},<EOF>", 135))
    def test_37(self):
        self.assertTrue(TestLexer.test("{2.3, 4.2, 102e3}", "{,2.3,,,4.2,,,102e3,},<EOF>", 136))
    def test_38(self):
        self.assertTrue(TestLexer.test("true&&false", "true,&&,false,<EOF>", 137))
    def test_39(self):
        self.assertTrue(TestLexer.test("int[5] a;", "int,[,5,],a,;,<EOF>", 138))
    def test_40(self):
        self.assertTrue(TestLexer.test("new class();", "new,class,(,),;,<EOF>", 139))
    def test_41(self):
        self.assertTrue(TestLexer.test("x:=9%2;", "x,:=,9,%,2,;,<EOF>", 140))
    def test_42(self):
        self.assertTrue(TestLexer.test("35/*a comment*/36", "35,36,<EOF>", 141))
    def test_43(self):
        self.assertTrue(TestLexer.test("a[3+x.foo(2)] := a[b[2]] +3;", "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>", 142))
    def test_44(self):
        self.assertTrue(TestLexer.test("x.b[2] := x.m()[3];", "x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,<EOF>", 143))
    def test_45(self):
        self.assertTrue(TestLexer.test("if x>=y then", "if,x,>=,y,then,<EOF>", 144))
    def test_46(self):
        self.assertTrue(TestLexer.test("\"/*comment in string*/\"", "\"/*comment in string*/\",<EOF>", 145))
    def test_47(self):
        self.assertTrue(TestLexer.test("this.aPI := 3.14; #PI", "this,.,aPI,:=,3.14,;,<EOF>", 146))
    def test_48(self):
        self.assertTrue(TestLexer.test("io.writeStrLn(\"Expression is true\");", "io,.,writeStrLn,(,\"Expression is true\",),;,<EOF>", 147))
    def test_49(self):
        self.assertTrue(TestLexer.test("for i := 1 to 100 do", "for,i,:=,1,to,100,do,<EOF>", 148))
    def test_50(self):
        self.assertTrue(TestLexer.test("a!=b||c==d", "a,!=,b,||,c,==,d,<EOF>", 149))
    def test_51(self):
        self.assertTrue(TestLexer.test("s:Shape;", "s,:,Shape,;,<EOF>", 150))
    def test_52(self):
        self.assertTrue(TestLexer.test("s := new Rectangle(3,4);", "s,:=,new,Rectangle,(,3,,,4,),;,<EOF>", 151))
    def test_53(self):
        self.assertTrue(TestLexer.test("/*comment\n*/*/", "*,/,<EOF>", 152))
    def test_54(self):
        self.assertTrue(TestLexer.test("/*/*comment#block*/*/", "*,/,<EOF>", 153))
    def test_55(self):
        self.assertTrue(TestLexer.test("line1#/*\n*/line2", "line1,*,/,line2,<EOF>", 154))
    def test_56(self):
        self.assertTrue(TestLexer.test("dfds_32 != 32_dfds", "dfds_32,!=,32,_dfds,<EOF>", 155))
    def test_57(self):
        self.assertTrue(TestLexer.test("a:=\"hel\\lo\";", "a,:=,Illegal Escape In String: \"hel\\l", 156))
    def test_58(self):
        self.assertTrue(TestLexer.test("\"dshf\\men", "Unclosed String: \"dshf\\men", 157))
    def test_59(self):
        self.assertTrue(TestLexer.test("\"98$\"98$", "\"98$\",98,Error Token $", 158))
    def test_60(self):
        self.assertTrue(TestLexer.test("\"na\tdi\\t\\xdw\"", "Illegal Escape In String: \"na\tdi\\t\\x", 159))
    def test_61(self):
        self.assertTrue(TestLexer.test("\"a string\\\"", "Unclosed String: \"a string\\\"", 160))
    def test_62(self):
        self.assertTrue(TestLexer.test("\"a string\\", "Unclosed String: \"a string\\", 161))
    def test_63(self):
        self.assertTrue(TestLexer.test("\"a string\\d", "Unclosed String: \"a string\\d", 162))
    def test_64(self):
        self.assertTrue(TestLexer.test("\sjkdf923:!><+d_3", "\,sjkdf923,:,!,>,<,+,d_3,<EOF>", 163))
    def test_65(self):
        self.assertTrue(TestLexer.test("Intarray[i] := i + 1;", "Intarray,[,i,],:=,i,+,1,;,<EOF>", 164))
    def test_66(self):
        self.assertTrue(TestLexer.test("def test_66(self):", "def,test_66,(,self,),:,<EOF>", 165))
    def test_67(self):
        self.assertTrue(TestLexer.test("3.23jfd5", "3.23,jfd5,<EOF>", 166))
    def test_68(self):
        self.assertTrue(TestLexer.test("3.23e12jfd5.4", "3.23e12,jfd5,.,4,<EOF>", 167))
    def test_69(self):
        self.assertTrue(TestLexer.test("____t____-2", "____t____,-,2,<EOF>", 168))
    def test_70(self):
        self.assertTrue(TestLexer.test("x:=-123+543", "x,:=,-,123,+,543,<EOF>", 169))
    def test_71(self):
        self.assertTrue(TestLexer.test("\"string1\"^\"string2\"", "\"string1\",^,\"string2\",<EOF>", 170))
    def test_72(self):
        self.assertTrue(TestLexer.test("float a:=87.3\\12;", "float,a,:=,87.3,\\,12,;,<EOF>", 171))
    def test_73(self):
        self.assertTrue(TestLexer.test("int[3] a := {1,2,3};", "int,[,3,],a,:=,{,1,,,2,,,3,},;,<EOF>", 172))
    def test_74(self):
        self.assertTrue(TestLexer.test("class Rectangle extends Shape", "class,Rectangle,extends,Shape,<EOF>", 173))
    def test_75(self):
        self.assertTrue(TestLexer.test("return this.length*this.width;", "return,this,.,length,*,this,.,width,;,<EOF>", 174))
    def test_76(self):
        self.assertTrue(TestLexer.test("s := new Rectangle(3,4);", "s,:=,new,Rectangle,(,3,,,4,),;,<EOF>", 175))
    def test_77(self):
        self.assertTrue(TestLexer.test("a:=\"hekdslf\\fkd\";", "a,:=,\"hekdslf\\fkd\",;,<EOF>", 176))
    def test_78(self):
        self.assertTrue(TestLexer.test("a:=\"hekdslf\\ekd\";", "a,:=,Illegal Escape In String: \"hekdslf\\e", 177))
    def test_79(self):
        self.assertTrue(TestLexer.test("a:=\"hekdslf\\fkd\\\";", "a,:=,Unclosed String: \"hekdslf\\fkd\\\";", 178))
    def test_80(self):
        self.assertTrue(TestLexer.test("a:=\"hek\"^\"dke\\n\";", "a,:=,\"hek\",^,\"dke\\n\",;,<EOF>", 179))
    def test_81(self):
        self.assertTrue(TestLexer.test("3<4&5>6", "3,<,4,Error Token &", 180))
    def test_82(self):
        self.assertTrue(TestLexer.test("3<4|5>6", "3,<,4,Error Token |", 181))
    def test_83(self):
        self.assertTrue(TestLexer.test("3<4&&5>6", "3,<,4,&&,5,>,6,<EOF>", 182))
    def test_84(self):
        self.assertTrue(TestLexer.test("3<4||5>6", "3,<,4,||,5,>,6,<EOF>", 183))
    def test_85(self):
        self.assertTrue(TestLexer.test("1+2=3", "1,+,2,=,3,<EOF>", 184))
    def test_86(self):
        self.assertTrue(TestLexer.test("sdj_Sjsdj32", "sdj_Sjsdj32,<EOF>", 185))
    def test_87(self):
        self.assertTrue(TestLexer.test("9e8fj3.24,34sef3", "9e8,fj3,.,24,,,34,sef3,<EOF>", 186))
    def test_88(self):
        self.assertTrue(TestLexer.test("012jsd32e+9fd", "012,jsd32e,+,9,fd,<EOF>", 187))
    def test_89(self):
        self.assertTrue(TestLexer.test("i+=1;", "i,+,=,1,;,<EOF>", 188))
    def test_90(self):
        self.assertTrue(TestLexer.test("dekd\"sef\"", "dekd,\"sef\",<EOF>", 189))
    def test_91(self):
        self.assertTrue(TestLexer.test("shej\"sejh\\r", "shej,Unclosed String: \"sejh\\r", 190))
    def test_92(self):
        self.assertTrue(TestLexer.test("\"jheds\"kd\"ekd\\gdk\"", "\"jheds\",kd,Illegal Escape In String: \"ekd\\g", 191))
    def test_93(self):
        self.assertTrue(TestLexer.test("\"ke#khds\"kd#kdh", "\"ke#khds\",kd,<EOF>", 192))
    def test_94(self):
        self.assertTrue(TestLexer.test("ok/*d\"kdh\\mds\"", "ok,/,*,d,Illegal Escape In String: \"kdh\m", 193))
    def test_95(self):
        self.assertTrue(TestLexer.test("/*dk\nsjkd!@&^$&#hdfkjsb2834", "/,*,dk,sjkd,!,Error Token @", 194))
    def test_96(self):
        self.assertTrue(TestLexer.test("@kidie", "Error Token @", 195))
    def test_97(self):
        self.assertTrue(TestLexer.test("[]()/.,:)", "[,],(,),/,.,,,:,),<EOF>", 196))
    def test_98(self):
        self.assertTrue(TestLexer.test("SIEJ23[iJ2k]", "SIEJ23,[,iJ2k,],<EOF>", 197))
    def test_99(self):
        self.assertTrue(TestLexer.test("J39dkeiID\"", "J39dkeiID,Unclosed String: \"", 198))
    def test_100(self):
        self.assertTrue(TestLexer.test("123_abc", "123,_abc,<EOF>", 199))