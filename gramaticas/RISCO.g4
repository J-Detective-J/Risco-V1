grammar RISCO; 


// Sección de miembros del parser
// Permite compartir estado dentro del parser generado.
// En RISCO la memoria real se maneja en el VisitanteEvaluador,
// este bloque queda como punto de extensión.


@parser::members {
    # Memoria para variables
    memoria = {}
}

// Programa principal - acepta saltos de línea entre sentencias
programa: (NL* sentencia NL*)* EOF;

sentencia
    : declaracion_variable
    | asignacion
    | expresion_stmt
    | for_stmt
    | print_stmt
    ;
print_stmt
    : PRINT '(' expresion ')' NL
    ;


declaracion_variable
    : 'val' IDENTIFICADOR '=' expresion NL
    | 'var' IDENTIFICADOR '=' expresion NL
    ;

asignacion
    : IDENTIFICADOR '=' expresion NL
    ;

expresion_stmt
    : expresion NL
    ;

for_stmt
    : 'for' IDENTIFICADOR 'in' expresion ':' NL
      (NL* sentencia)*
      END  NL
    ;

// Expresiones con precedencia (de menor a mayor)
expresion
    : or_logico
    ;

or_logico
    : and_logico ('||' and_logico)*
    ;

and_logico
    : igualdad ('&&' igualdad)*
    ;

igualdad
    : relacional (('==' | '!=') relacional)*
    ;

relacional
    : suma (('>' | '<' | '>=' | '<=') suma)*
    ;

suma
    : comparacion (('+' | '-') comparacion)*
    ;

comparacion
    : termino ('in' termino)?
    ;

termino
    : potencia (('*' | '/' | '%') potencia)*
    ;

potencia
    : primario
    | primario '^' potencia
    ;

primario
    : NUMERO
    | DECIMAL
    | STRING
    | BOOLEANO
    | NULL
    | lista
    | IDENTIFICADOR
    | '(' expresion ')'
    | '-' primario  // negativo unario
    | '!' primario  // not lógico
    ;

lista
    : '[' (expresion (',' expresion)*)? ']'
    ;

// Palabras reservadas — DEBEN ir antes de IDENTIFICADOR
FOR          : 'for';
IN           : 'in';
END          : 'end';
VAL          : 'val';
VAR          : 'var';
PRINT        : 'print';

// Operadores de dos caracteres
AND  : '&&';
OR   : '||';
EQ   : '==';
NEQ  : '!=';
GTE  : '>=';
LTE  : '<=';

// Tokens léxicos
NUMERO : DIGITO+;
DECIMAL : DIGITO+ '.' DIGITO+;
STRING : '"' ( ~["\r\n] | '\\"' )* '"'; 
BOOLEANO : 'true' | 'false';
NULL : 'null';
IDENTIFICADOR : LETRA (LETRA | DIGITO | '_')*;

// Fragmentos
fragment LETRA : [a-zA-ZáéíóúñÁÉÍÓÚÑ];
fragment DIGITO : [0-9];

// Saltos de línea
NL : ('\r'? '\n')+;

// Espacios en blanco
WS : [ \t]+ -> skip;

// Comentarios
COMENTARIO_LINEA : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/-' .*? '-/' -> skip;
COMENTARIO_DOC : '///' ~[\r\n]* -> skip;
