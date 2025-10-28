# MaterialUI LaTeX Theme

A clean, modern LaTeX theme inspired by Material Design principles and the Metropolis Beamer theme.

## Features

- **Material Design Color Palette**: Beautiful, accessible colors from Material Design
- **Modern Typography**: Uses Fira Sans Light for regular text, Fira Sans for bold, and Fira Mono for code
- **Mathematics Support**: Includes amsthm, mathtools, and unicode-math with FiraMath
- **Clean Code Listings**: Syntax highlighting with Material colors and consistent borders
- **Custom Box Generator**: Create styled mdframed environments with any color
- **Professional Styling**: Clean section formatting and improved spacing

## Requirements

- XeLaTeX (for font support)
- Fira Sans font family (Light and Regular weights)
- Fira Mono font
- FiraMath font

## Installation

Copy `theme.sty` to your LaTeX project directory and include it in your document:

```latex
\documentclass[10pt,a4paper]{article}
\usepackage{theme}
```

## Color Palette

The theme includes these Material Design colors:

- **materialBlue**: `#2196F3`
- **materialIndigo**: `#3F51B5`
- **materialGreen**: `#4CAF50`
- **materialOrange**: `#FF9800`
- **materialRed**: `#F44336`
- **materialGrey**: `#9E9E9E`
- **materialLightGrey**: `#F5F5F5`
- **materialDarkGrey**: `#616161`

## Usage

### Material Design Boxes

Create custom styled boxes using the `\definematerialbox` command:

```latex
\documentclass[10pt,a4paper]{article}
\usepackage{theme}

% Define custom box styles
\definematerialbox{notestyle}{Note}{materialBlue}
\definematerialbox{warningstyle}{Warning}{materialRed}
\definematerialbox{tipstyle}{Tip}{materialGreen}

\begin{document}

\begin{mdframed}[style=notestyle]
This is a note with a blue accent.
\end{mdframed}

\begin{mdframed}[style=warningstyle]
\textbf{Warning:} Important information here.
\end{mdframed}

\end{document}
```

**Command Syntax:**
```latex
\definematerialbox{stylename}{Title}{color}
```

- `stylename`: Unique name for the style (e.g., `notestyle`)
- `Title`: Text shown in the box header (e.g., `Note`)
- `color`: Any Material Design color or custom xcolor (e.g., `materialBlue`)

### Code Listings

The theme automatically configures code listings with borders and Material colors:

```latex
\begin{lstlisting}[language=Python]
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
\end{lstlisting}
```

### Mathematics

The theme includes amsthm, mathtools, and unicode-math:

```latex
% Theorem environments
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}

\begin{theorem}
For all $n \in \mathbb{N}$, we have $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$.
\end{theorem}

% Math with mathtools
\begin{equation}
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\end{equation}
```

## Example Document

See `sample.tex` for a complete example demonstrating all features.

## License

MIT License - feel free to use and modify for your projects.
