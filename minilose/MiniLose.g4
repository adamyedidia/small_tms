grammar MiniLose;

prog: (command)* ;
command:  (funcdef | procdef | declare | nondefcommand)  ;

nondefprog: (nondefcommand)* ;
nondefcommand:  (funcproccall | whileloop | forloop | ifstate | assign | returnstate)  ;

funcdef: 'func' funcprocbody ;
procdef: 'proc' funcprocbody ;

funcprocbody:  funcproccallbody  '{' nondefprog '}' ;

declare: natdecl ;

natdecl: 'nat'  VAR  ';' ;

funcproccall: funcproccallbody  ';' ;

funcproccallbody: VAR  '(' ( VAR  ',' )* VAR  ')' ;

whileloop: 'while'  '('  expr  ')'  '{' nondefprog '}' ;

forloop: 'for'  '('  nondefcommand  ';'  expr  ';'  nondefcommand  ')'  '{' nondefprog '}' ;

ifstate: 'if'  '('  expr  ')'  '{' nondefprog '}' ;

assign: VAR  '='  expr  ';' ;

returnstate: ('return' | 'halt')  ';' ;

expr:   expr ('*'|'/') expr
    |   expr ('+'|'-') expr 
    |   expr ('<'|'>'|'=='|'>='|'<='|'!=') expr
    |   INT
    |   '(' expr ')'
    |  VAR
    ;

WS : [\t\n\r ]+ -> skip;
VAR     : [a-zA-Z_]+ ;
INT     : [0-9]+ ;

