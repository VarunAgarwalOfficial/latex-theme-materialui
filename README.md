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

### Custom Boxes

Use mdframed with custom styles:

```latex
\mdfdefinestyle{answerstyle}{
    backgroundcolor=materialIndigo!8,
    linecolor=materialIndigo!60,
    linewidth=1pt,
    frametitle={Answer},
    frametitlebackgroundcolor=materialIndigo!20,
    frametitlefont=\bfseries\color{materialIndigo}
}

\begin{mdframed}[style=answerstyle]
Your content here
\end{mdframed}
```

## License

MIT License - feel free to use and modify for your projects.

## Contributing

Contributions welcome! Please submit issues and pull requests.
