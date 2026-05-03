# 🎵 Lyrics Printer

A Python terminal tool that prints song lyrics **beautifully** using ANSI escape codes — rich colors, hearts, sparkles, music notes, animations, and styled typography, right in your terminal.

---

## ✨ Features

- **5 themes** — Romantic, Sad, Neon, Golden, Devotional, Gradient
- **Hearts & symbols** — ♥ ♡ ❥ ✨ ★ ✦ ♫ ♪ ✿ ◆ in headers & footers
- **Section labels** — tag lines with `#Chorus`, `#Verse 1`, `#Bridge` etc.
- **4 display styles** — Gradient, Typing, Fade, Static
- **Gradient color cycling** per theme
- **Centered layout** with 62-char stage width
- **Configurable line delay** — control the pace
- **6 ready-to-use song templates** — just paste your lyrics

---

## 🖥️ Preview (Romantic Theme)

```
══════════════════════════════════════════════════════════════
                      ♥  Rag Rag  ❥
                    — Gajendra Verma —
══════════════════════════════════════════════════════════════

                 [ ♥ Verse 1 ❥ ]

              Rag rag woh samaya mere...
                      Rag Rag

                 [ ♥ Chorus ❥ ]

              Rag rag woh samaya mere...

──────────────────────────────────────────────────────────────
                   ❥  ♥  ❥  ♥  ❥
                    end of lyrics
──────────────────────────────────────────────────────────────
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/subhobhai943/lyrics-printer.git
cd lyrics-printer
python lyrics_printer.py
```

No dependencies — pure Python standard library.

---

## 🎨 Themes

| Theme | Colors | Best For | Symbols |
|---|---|---|---|
| `gradient` | Red → Purple → Gold → Pink → Blue | General | ♪ ♫ |
| `romantic` | Rose Pink → Deep Red → Warm Gold | Love songs | ♥ ❥ |
| `sad` | Soul Purple → Sky Blue → Lilac | Sad songs | ♡ ☆ |
| `neon` | Sky Blue → Mint → Rose Pink | Lo-fi / Pop | ✦ ✨ |
| `golden` | Warm Gold → Dusk Orange | Classic | ★ ◆ |
| `devotional` | Gold → Orange → Pink | Bhajans | ✿ ✤ |

---

## 🎭 Display Styles

| Style | Effect |
|---|---|
| `'gradient'` | Each line cycles through theme colors |
| `'typing'` | Typewriter character-by-character |
| `'fade'` | Line progressively reveals left to right |
| `'static'` | Clean single-color white |

---

## 🎵 Section Labels

Tag any line with `#` to render it as a decorated section label:

```python
LYRICS = """
#Verse 1
First line here
Second line here

#Chorus
Chorus line here
"""
```

This prints as:
```
           [ ♥ Verse 1 ❥ ]

        First line here
        Second line here

           [ ♥ Chorus ❥ ]
```

---

## 📁 Song Templates

| File | Theme | Style | Use For |
|---|---|---|---|
| `songs/sahiba_template.py` | romantic | fade | Romantic Hindi songs |
| `songs/romantic_song_template.py` | romantic | gradient | Love songs |
| `songs/sad_song_template.py` | sad | typing | Sad / emotional songs |
| `songs/devotional_template.py` | devotional | fade | Bhajans / devotional |
| `songs/neon_lofi_template.py` | neon | typing | Lo-fi / pop tracks |
| `songs/example_song.py` | gradient | gradient | General purpose |

To use any template:
1. Open the file
2. Set `SONG_TITLE` and `SONG_ARTIST`
3. Paste your lyrics into the `LYRICS` string
4. Add `#Chorus`, `#Verse 1` etc. for section labels
5. Run: `python songs/sahiba_template.py`

---

## 🎨 Symbol Reference

```python
HEART        = '♥'   # Full heart
HEART_OPEN   = '♡'   # Open heart
HEART_RIBBON = '❥'   # Ribbon heart
SPARKLE      = '✨'   # Sparkle
STAR         = '★'   # Filled star
STAR_OPEN    = '☆'   # Open star
SPARK        = '✦'   # 4-point spark
NOTE         = '♫'   # Double note
NOTE2        = '♪'   # Single note
FLOWER       = '✿'   # Flower
DIAMOND      = '◆'   # Diamond
```

---

## 📌 Requirements

- Python 3.6+
- A terminal with ANSI support (Linux, macOS, Windows Terminal)

---

*Built with ♥ and ANSI escape codes.*
