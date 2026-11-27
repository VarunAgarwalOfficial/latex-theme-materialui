.PHONY: check contrast lint

check: contrast
	latexmk -xelatex -interaction=nonstopmode -halt-on-error sample.tex

contrast:
	python3 contrast.py

lint:
	chktex -q theme.sty sample.tex
