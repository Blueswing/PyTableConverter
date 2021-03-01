/* 
 
 Simplified JSON grammar
 
 Taken from "The Definitive ANTLR 4 Reference" by Terence Parr 
 Derived from http://json.org
 
 */

grammar JSONTable;

table: arr EOF?;

arr:
	'[' simpleObj (',' simpleObj)* ']'		# objTable
	| '[' simpleArr (',' simpleArr)* ']'	# arrTable
	| '[' ']'								# arrTable;

simpleObj: '{' pair (',' pair)* '}' | '{' '}';
simpleArr: '[' simpleValue (',' simpleValue)* ']' | '[' ']';

pair: STRING ':' simpleValue;

simpleValue: STRING | INT | FLOAT | TRUE | FALSE | NULL;

TRUE: 'true';
FALSE: 'false';
NULL: 'null';

STRING: '"' (ESC | SAFECODEPOINT)* '"';

fragment ESC: '\\' (["\\/bfnrt] | UNICODE);
fragment UNICODE: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];
fragment SAFECODEPOINT: ~ ["\\\u0000-\u001F];

FLOAT: '-'? INT '.' [0-9]+ | '-'? INT ('.' [0-9]+)? EXP;

// no leading zeros
INT: '0' | [1-9] [0-9]*;

fragment EXP: [Ee] [+\-]? INT;

// \- since - means "range" inside [...]

WS: [ \t\n\r]+ -> skip;