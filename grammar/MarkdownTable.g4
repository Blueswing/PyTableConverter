grammar MarkdownTable;

table: header sepLine body EOF?;

header: row '\n';

sepLine: '|' (BAR '|')+ '\n';

body: (row '\n')* row '\n'?;

row:  '|' (item '|')+ ;

item: STRING | ;

BAR: ':'? '-'+ ':'?;

STRING: ( '\\\\' | '\\|' | ~( '\\' | '|' ) )+;

WS: [ \t\n\r] -> skip;
