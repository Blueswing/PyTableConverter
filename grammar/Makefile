ifeq ($(OS),Windows_NT)
    $(error this make file does not support Windows)
else
	RM := rm
	RD := rm -rf
endif

ANTLR=java -jar /var/lib/antlr/antlr-4.8-complete.jar
PACKAGE_ROOT=../tableconverter
OUTPUT_DIR=$(PACKAGE_ROOT)/autogen
TARGET_LANGUAGE=Python3
ANTLR_PARAMS=-o $(OUTPUT_DIR) -Dlanguage=$(TARGET_LANGUAGE)

.PHONY: all json html md csv clean

all: csv json md html
	echo '__author__ = """Yeefea"""' > $(OUTPUT_DIR)/__init__.py

csv: 
	$(ANTLR) CSV.g4 $(ANTLR_PARAMS)

json:
	$(ANTLR) JSONTable.g4 $(ANTLR_PARAMS)

md:
	$(ANTLR) MarkdownTable.g4 $(ANTLR_PARAMS)

html:
	$(ANTLR) HTMLLexer.g4 $(ANTLR_PARAMS)
	$(ANTLR) HTMLTable.g4 $(ANTLR_PARAMS)

clean:
	-(cd $(PACKAGE_ROOT) && $(RD) autogen)
