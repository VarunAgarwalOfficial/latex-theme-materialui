# Status

Status: complete, archived 27 November 2026.

- Tested: `make check` runs `contrast.py`, which fails if any text colour is under 4.5:1 on its background, then builds `sample.tex` with XeLaTeX. Both run in CI.
- Contrast: the lowest pair is 4.91:1 (the title of an orange box). Before 27 November 2026, links were 2.16:1 and box titles 1.70 to 2.46:1.
- No further work is planned. For new documents, Typst or the Metropolis theme are maintained alternatives.
