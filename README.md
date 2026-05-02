# 🎵 Lyrics Printer

A Python terminal tool that prints song lyrics **beautifully** using ANSI escape codes — rich colors, animations, and styled typography, right in your terminal.

Inspired by the vibe of coding-in-style content creators.

---

## ✨ Features

- **Gradient color cycling** — each lyric line glows in a different rich color
- **Typewriter effect** — characters appear one by one for dramatic feel
- **Fade-in effect** — lines slide into view progressively
- **Centered layout** — lyrics are centered like a stage display
- **Custom color palette** — Deep Red, Soul Purple, Warm Gold, Mist White, Rose Pink, Sky Blue & more
- **Configurable line delay** — control the pace of lyric display
- **Plug-in your own song** — just fill in title, artist, and lyrics

---

## 🖥️ Preview

```
════════════════════════════════════════════════════════════
                    ♪  Rag Rag  ♪
                   — Gajendra Verma —
════════════════════════════════════════════════════════════

              Rag rag woh samaya mere...
                       Rag Rag

              Rag rag woh samaya mere...

            Har pal tujhe hi dhundhta hoon main
```

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/subhobhai943/lyrics-printer.git
cd lyrics-printer

# Run the demo song
python lyrics_printer.py
```

No dependencies required — pure Python standard library.

---

## 🎨 Display Styles

Change the `style` parameter in `print_lyrics()` to switch look:

| Style | Description |
|---|---|
| `'gradient'` | Cycles through vibrant ANSI colors (default) |
| `'typing'` | Typewriter character-by-character effect |
| `'fade'` | Progressive line reveal |
| `'static'` | Clean, single-color white |

```python
print_lyrics(lines, style='typing', line_delay=1.2)
```

---

## 🎵 Add Your Own Song

1. Copy `songs/example_song.py`
2. Fill in `SONG_TITLE`, `SONG_ARTIST`, and `LYRICS`
3. Run it:

```bash
python songs/my_song.py
```

---

## 🎨 Color Palette

```python
DEEP_RED    = '\033[38;5;88m'
SOUL_PURPLE = '\033[38;5;54m'
WARM_GOLD   = '\033[38;5;136m'
MIST_WHITE  = '\033[38;5;251m'
ROSE_PINK   = '\033[38;5;211m'
SKY_BLUE    = '\033[38;5;75m'
SAGE_GREEN  = '\033[38;5;65m'
DUSK_ORANGE = '\033[38;5;172m'
```

Customize any color using [256-color ANSI codes](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit).

---

## 📁 Project Structure

```
lyrics-printer/
├── lyrics_printer.py   # Core engine: colors, effects, printing
├── songs/
│   └── example_song.py # Template for adding your own songs
└── README.md
```

---

## 📌 Requirements

- Python 3.6+
- A terminal that supports ANSI escape codes (Linux, macOS, Windows Terminal)

---

*Built with ♥ and ANSI escape codes.*
