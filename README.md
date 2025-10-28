# MaterialUI LaTeX Theme

A clean, modern LaTeX theme inspired by Material Design principles and the Metropolis Beamer theme.

## Features

- **Material Design Color Palette**: Beautiful, accessible colors from Material Design
- **Modern Typography**: Uses Fira Sans and Fira Mono fonts with FiraMath for mathematics
- **Clean Code Listings**: Syntax highlighting with Material colors
- **Professional Tables**: Booktabs integration for publication-quality tables
- **Custom Boxes**: Styled mdframed environments for answers, corollaries, and more
- **Improved Spacing**: Carefully tuned spacing for readability

## Requirements

- XeLaTeX (for font support)
- Fira Sans font family
- Fira Mono font
- FiraMath font

## Installation

Simply copy `theme.sty` to your LaTeX project directory and include it in your document:

```latex
\documentclass{article}
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

### Code Listings

The theme automatically configures listings with Material colors:

```latex
\begin{lstlisting}[language=Python]
def hello_world():
    print("Hello, World!")
\end{lstlisting}
```

### Material Design Boxes

The theme provides a convenient command to create styled mdframed environments:

```latex
% Define custom box styles
\definematerialbox{answerstyle}{Answer}{materialIndigo}
\definematerialbox{corollarystyle}{Corollary}{materialOrange}
\definematerialbox{notestyle}{Note}{materialBlue}

% Use the boxes
\begin{mdframed}[style=answerstyle]
Your answer here
\end{mdframed}

\begin{mdframed}[style=corollarystyle]
Your corollary here
\end{mdframed}
```

**Command Syntax:**
```latex
\definematerialbox{stylename}{Title}{color}
```

- `stylename`: The name you want to give the style
- `Title`: The text shown in the box header
- `color`: Any Material Design color or custom color defined with xcolor

## License

MIT License - feel free to use and modify for your projects.

## Contributing

Contributions welcome! Please submit issues and pull requests.
