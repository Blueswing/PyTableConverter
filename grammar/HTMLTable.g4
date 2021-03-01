/*
 HTML table
*/

parser grammar HTMLTable;

options {
	tokenVocab = HTMLLexer;
}

table:
	TAG_OPEN TAG_TABLE htmlAttribute* (
		TAG_CLOSE (
			htmlContent TAG_OPEN TAG_SLASH TAG_TABLE TAG_CLOSE
		)?
		| TAG_SLASH_CLOSE
	) EOF?;

htmlElement:
	TAG_OPEN tag = TAG_NAME htmlAttribute* (
		TAG_CLOSE content = htmlContent TAG_OPEN TAG_SLASH TAG_NAME TAG_CLOSE
		| TAG_SLASH_CLOSE
	)			# NormalTag
	| SCRIPTLET	# Ignored
	| script	# Ignored
	| style		# Ignored;

htmlContent:
	htmlChardata? (
		(htmlElement | CDATA | htmlComment) htmlChardata?
	)*;

htmlAttribute: TAG_NAME (TAG_EQUALS ATTVALUE_VALUE)?;

htmlChardata: HTML_TEXT | SEA_WS;

htmlMisc: htmlComment | SEA_WS;

htmlComment: HTML_COMMENT | HTML_CONDITIONAL_COMMENT;

script: SCRIPT_OPEN (SCRIPT_BODY | SCRIPT_SHORT_BODY);

style: STYLE_OPEN (STYLE_BODY | STYLE_SHORT_BODY);