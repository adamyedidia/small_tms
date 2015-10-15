grammar Lose;

prog: trueprog ;
trueprog: (command)* EOF ;
command:  (funcdef | procdef | declare | nondefcommand)  ;

nondefprog: (nondefcommand)* ;
nondefcommand:  (funcproccall | whileloop | forloop | ifstate | ifelsestate | assign | returnstate | printstate)  ;

funcdef: 'func' funcprocbody ;
procdef: 'proc' funcprocbody ;

funcprocbody:  funcproccallbody  '{' nondefprog '}' ;

declare: (natdecl | signdecl | listdecl | list2decl) ;

natdecl: 'nat'  VAR  ('=' expr)? ';';
signdecl: 'signed'  VAR ('=' expr)? ';' ;
listdecl: 'list'  VAR ('=' expr)? ';' ;
list2decl: 'list2'  VAR ('=' expr)? ';' ;

funcproccall: funcproccallbody  ';' ;

funcproccallbody: VAR  '(' ( VAR  ',' )* VAR  ')' ;

whileloop: 'while'  '('  whileexpr  ')'  '{' whilenondefprog '}' ;

forloop: 'for'  '('  nondefcommand  ';'  expr  ';'  nondefcommand  ')'  '{' nondefprog '}' ;

ifstate: 'if'  '('  ifexpr  ')'  '{' ifnondefprog '}' ;

printstate: 'print' VAR ';' ;

ifelsestate: 'ifelse' '(' ifelseexpr ')' '{' ifelsenondefprog '}' '{' elsenondefprog '}' ;

ifelsenondefprog: nondefprog ;
elsenondefprog: nondefprog ;
ifnondefprog: nondefprog ; 
whilenondefprog: nondefprog ;

ifelseexpr: expr ;
ifexpr: expr ;
whileexpr: expr ;

assign: VAR  '='  expr  ';' ;

returnstate: ('return' | 'halt')  ';' ;

expr:   expr OPERATOR_MUL_DIV expr
    |   expr OPERATOR_ADD_SUB expr 
    |   expr OPERATOR_COMPARE expr
    |   expr OPERATOR_BOOLEAN expr
    |   OPERATOR_NOT expr
    |   INT
    |   '(' expr ')'
    |  VAR
    ;

OPERATOR_MUL_DIV: ('*' | '/' | '%') ;
OPERATOR_ADD_SUB: ('+' | '-') ;
OPERATOR_COMPARE: ('==' | '!=' | '>' | '<' | '>=' | '<=') ;
OPERATOR_BOOLEAN: ('&' | '|') ;
OPERATOR_NOT: ('!') ;

COMMENT : '/*'.*?'*/' -> skip;
WS : [\t\n\r ]+ -> skip;
VAR     : [a-zA-Z_]+ ;
INT     : [0-9]+ ;

