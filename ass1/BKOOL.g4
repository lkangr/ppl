grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (CLASSTYPE ID (EXTENDS ID)? LP (attr|meth)* RP)+ EOF; 

attr: ((STATIC FINAL?) | (FINAL STATIC?))? typ ID (EQOP expr)? (COMMA ID (EQOP expr)?)* SEMI;

meth: (STATIC? typ)? ID LB (typ ID (COMMA ID)* (SEMI typ ID (COMMA ID)*)*)? RB blockstm;

expr: expr (LT | GT | LTE | GTE) expr | expr1;

expr1: expr1 (EQ | NEQ) expr1 | expr2;

expr2: expr2 (LAND | LOR) expr3 | expr3;

expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;

expr4: expr4 (MULOP | IDIVOP | FDIVOP | MODOP) expr5 | expr5;

expr5: expr5 CON expr6 | expr6;

expr6: LNOT expr6 | expr7;

expr7: (ADDOP | SUBOP) expr7 | expr8;

expr8: expr9 LSB expr RSB | expr9;

expr9: expr9 DOT ID (LB (expr (COMMA expr)*)? RB)? | expr10;

expr10: NEW ID LB (expr (COMMA expr)*)? RB | expr11;	

expr11: INTLIT | FLOATLIT | boollit | STRINGLIT | arraylit | ID | THIS | LB expr RB;

blockstm: LP varclr* stmt* RP;

varclr: FINAL? typ ID (EQOP expr)? (COMMA ID (EQOP expr)?)* SEMI;

stmt: blockstm | asmstm | ifstm | forstm | brkstm | constm | rtstm | invstm;

asmstm: lhs ASM expr SEMI;

lhs: expr9 LSB expr RSB | expr9 DOT ID | ID;

ifstm: IF expr THEN stmt (ELSE stmt)?;

forstm: FOR ID ASM expr (TO | DOWNTO) expr DO stmt;

brkstm: BREAK SEMI;

constm: CONTINUE SEMI;

rtstm: RETURN expr SEMI;

invstm: expr DOT ID LB (expr (COMMA expr)*)? RB SEMI;

typ: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | arraytype | VOIDTYPE | ID;

arraytype: (INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | ID) LSB INTLIT RSB;

arraylit: LP ((INTLIT (COMMA INTLIT)*) | (FLOATLIT (COMMA FLOATLIT)*) | (boollit (COMMA boollit)*) | STRINGLIT (COMMA STRINGLIT)*) RP;

boollit: BTRUE | BFALSE;

INTTYPE: 'int';

VOIDTYPE: 'void';

BOOLTYPE: 'boolean';

FLOATTYPE: 'float';

STRINGTYPE: 'string';

NILTYPE: 'nil';

CLASSTYPE: 'class';

BREAK: 'break';

CONTINUE: 'continue';

DO: 'do';

ELSE: 'else';

EXTENDS: 'extends';

IF: 'if';

NEW: 'new';

THEN: 'then';

FOR: 'for';

RETURN: 'return';

BTRUE: 'true';

BFALSE: 'false';

THIS: 'this';

FINAL: 'final';

STATIC: 'static';

TO: 'to';

DOWNTO: 'downto';

BLOCKCMT: '/*' .*? '*/' -> skip;

LINECMT: '#' .*? ('\n' | EOF) -> skip;

ID: [_a-zA-Z][_a-zA-Z0-9]*;

ASM: ':=';

EQOP: '=';

ADDOP: '+';

SUBOP: '-';

MULOP: '*';

FDIVOP: '/';

IDIVOP: '\\';

MODOP: '%';

NEQ: '!=';

EQ: '==';

LT: '<';

GT: '>';

LTE: '<=';

GTE: '>=';

LOR: '||';

LAND: '&&';

LNOT: '!';

CON: '^';

LSB: '[';

RSB: ']';

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

COLON: ':';

DOT: '.';

COMMA: ',';

INTLIT: [0-9]+;

FLOATLIT: [0-9]+ (('.' [0-9]*) | (('.' [0-9]*)?([eE][+-]?[0-9]+)));

STRINGLIT: '"' ((~[\n"\\]) | ('\\' [bfrnt"\\]))* '"';

WS: [ \t\f\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' ((~[\n"]) | ('\\' [bfrnt"\\]))* ('\n' | EOF) {raise UncloseString(self.text)};

ILLEGAL_ESCAPE: '"' ((~[\n"\\]) | ('\\' [bfrnt"\\]))* '\\' ~[bfrnt"\\] {raise IllegalEscape(self.text)};