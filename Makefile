.PHONY: check lint

check:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error sample.tex

lint:
	chktex -q theme.sty sample.tex
