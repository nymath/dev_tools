LATEX = xelatex
TARGET = main

all = start

start: $(TARGET)

$(TARGET): $(TARGET).tex
	@mkdir -p ./build
	@$(LATEX) -output-directory=./build $@.tex
	@bibtex ./build/$@.aux
	@$(LATEX) -output-directory=./build $@.tex
	@$(LATEX) -output-directory=./build $@.tex
	@ln -sf ./build/$@.pdf $@.pdf

restart:
	@make stop
	@make start

stop:
	@rm -rf ./build

clean:
	@rm -rf ./build
