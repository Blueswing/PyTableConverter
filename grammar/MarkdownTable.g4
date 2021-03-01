grammar MarkdownTable;

table: header sepLine body EOF?;

header: row NL;

sepLine: '|' (BAR '|')+ NL;

body: (row NL)* row NL?;

row: '|' (item '|')+;

item: STRING |;

BAR: ':'? '-'+ ':'?;

STRING: ( '\\\\' | '\\|' | ~( '\\' | '|' | '\r' | '\n'))+;

NL: '\r'? '\n';

WS: [ \t\n\r] -> skip;
