grammar LPP;

prog: trueprog ;
trueprog: (command)* EOF ;
command:  (funcdef | procdef | declare | nondefcommand)  ;

nondefprog: (nondefcommand)* ;
nondefcommand:  (funcproccall | whileloop | forloop | ifstate | ifelsestate | assign | returnstate | printstate)  ;

funcdef: 'func' funcprocbody ;
procdef: 'proc' funcprocbody ;

funcprocbody:  funcproccallbody  '{' nondefprog '}' ;

declare: (intdecl | listdecl | list2decl) ;

intdecl: 'int'  VAR ('=' expr)? ';' ;
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

ifelseexpr: intexpr ;
ifexpr: intexpr ;
whileexpr: intexpr ;

expr: (intexpr | listexpr | list2expr) ;

assign: VAR  '='  expr  ';' ;

returnstate: ('return' | 'halt')  ';' ;



intexpr:   intexpr OPERATOR_MUL_DIV intexpr     // intop DONE DONE
    |   intexpr OPERATOR_ADD_SUB intexpr        // intop DONE DONE
    |   intexpr OPERATOR_COMPARE intexpr        // intop DONE DONE
    |   intexpr OPERATOR_BOOLEAN intexpr        // intop DONE DONE
    |   listexpr OPERATOR_INDEX intexpr                // listindex DONE DONE
    |   OPERATOR_NOT intexpr                    // intnot DONE DONE
    |   '(' intexpr ')'                         // DONE DONE
    |   OPERATOR_NEGATE intexpr                 // DONE
    |   OPERATOR_LENGTH listexpr                // DONE
    |   OPERATOR_LENGTH2 list2expr              // DONE
    |   INT                                     // intint DONE DONE
    |   VAR                                     // intvar DONE DONE
    ;
    
listexpr:
    |   list2expr OPERATOR_INDEX2 intexpr                // list2index
    |   listexpr OPERATOR_APPEND intexpr        // listappend
    |   listexpr OPERATOR_CONCAT listexpr       // listconcat
    |   '(' listexpr ')'                        
    |   '[' (intexpr ',')* intexpr ']'          // constlist
    |   '[' ']'                                 // emptylist
    |   VAR                                     // listvar
    ;

    // This is a giant hack!! Ask Zach how to fix this ASAP!
    
list2expr:
    |   list2expr OPERATOR_APPEND2 listexpr      // list2append
    |   list2expr OPERATOR_CONCAT2 list2expr     // list2concat
    |   '(' list2expr ')'
    |   ':' (listexpr ',')* listexpr ':'        // constlist2
    |   ':'                                     // emptylist2
    |  VAR                                      // list2var
    ;

OPERATOR_MUL_DIV: ('*' | '/' | '%') ;
OPERATOR_ADD_SUB: ('+' | '-') ;
OPERATOR_NEGATE: ('~') ;
OPERATOR_COMPARE: ('==' | '!=' | '>' | '<' | '>=' | '<=') ;
OPERATOR_BOOLEAN: ('&' | '|') ;
OPERATOR_NOT: ('!') ;
OPERATOR_APPEND: ('^') ;
OPERATOR_APPEND2: ('^*') ;
OPERATOR_CONCAT: ('||') ;
OPERATOR_CONCAT2: ('||*') ;
OPERATOR_INDEX: ('@') ;
OPERATOR_INDEX2: ('@*') ;
OPERATOR_LENGTH: ('#') ;
OPERATOR_LENGTH2: ('#*') ;

COMMENT : '/*'.*?'*/' -> skip;
WS : [\t\n\r ]+ -> skip;
VAR     : [a-zA-Z_] [a-zA-Z0-9_]* ;
INT     : [0-9]+ ;

