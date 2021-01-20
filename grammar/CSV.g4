grammar CSV;

fil: hdr ('\r'? '\n' row)* EOF?;
hdr: row;

row: field (',' field)*;

field: TEXT # text | STRING # string | # empty;

TEXT: ~[,\n\r"]+;
STRING: '"' ('""' | ~'"')* '"';
