import time
import sys
import os
import random

# ─── ANSI Color Palette ──────────────────────────────────────────────────────
DEEP_RED    = '\033[38;5;88m'
SOUL_PURPLE = '\033[38;5;54m'
WARM_GOLD   = '\033[38;5;136m'
MIST_WHITE  = '\033[38;5;251m'
ROSE_PINK   = '\033[38;5;211m'
SKY_BLUE    = '\033[38;5;75m'
SAGE_GREEN  = '\033[38;5;65m'
DUSK_ORANGE = '\033[38;5;172m'
SOFT_LILAC  = '\033[38;5;183m'
MINT        = '\033[38;5;121m'

BOLD   = '\033[1m'
DIM    = '\033[2m'
ITALIC = '\033[3m'
RESET  = '\033[0m'

# ─── Symbols & Decorations ───────────────────────────────────────────────────
HEART        = '\u2665'   # ♥
HEART_OPEN   = '\u2661'   # ♡
HEART_RIBBON = '\u2765'   # ❥
SPARKLE      = '\u2728'   # ✨
STAR         = '\u2605'   # ★
STAR_OPEN    = '\u2606'   # ☆
SPARK        = '\u2726'   # ✦
NOTE         = '\u266b'   # ♫
NOTE2        = '\u266a'   # ♪
FLOWER       = '\u273f'   # ✿
ROSE         = '\u2740'   # ✤  (asterism-like)
MOON         = '\U0001f319'  # 🌙
WIND         = '\u0d04'   # ༄ (Tibetan wind)
DIAMOND      = '\u25c6'   # ◆
DOT          = '\u2022'   # •

# ─── Themes ──────────────────────────────────────────────────────────────────
THEMES = {
    'gradient' : [DEEP_RED, SOUL_PURPLE, WARM_GOLD, ROSE_PINK, SKY_BLUE, DUSK_ORANGE],
    'romantic' : [ROSE_PINK, DEEP_RED, SOFT_LILAC, WARM_GOLD, ROSE_PINK, SOUL_PURPLE],
    'sad'      : [SOUL_PURPLE, SKY_BLUE, SOFT_LILAC, MIST_WHITE, SKY_BLUE, SOUL_PURPLE],
    'neon'     : [SKY_BLUE, MINT, ROSE_PINK, WARM_GOLD, MINT, SKY_BLUE],
    'golden'   : [WARM_GOLD, DUSK_ORANGE, WARM_GOLD, MIST_WHITE, WARM_GOLD, DUSK_ORANGE],
    'devotional': [WARM_GOLD, DUSK_ORANGE, ROSE_PINK, WARM_GOLD, MIST_WHITE, DUSK_ORANGE],
}

# Theme-matched header decorations
THEME_DECO = {
    'gradient'  : (NOTE2, NOTE),
    'romantic'  : (HEART, HEART_RIBBON),
    'sad'       : (HEART_OPEN, STAR_OPEN),
    'neon'      : (SPARK, SPARKLE),
    'golden'    : (STAR, DIAMOND),
    'devotional': (FLOWER, ROSE),
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def center_text(text: str, width: int = 62) -> str:
    return text.center(width)


def typing_effect(text: str, color: str = MIST_WHITE, delay: float = 0.04):
    sys.stdout.write(color + BOLD)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + '\n')


def fade_in_line(text: str, color: str = MIST_WHITE, steps: int = 6):
    chunk = max(1, len(text) // steps)
    for i in range(1, steps + 1):
        partial = text[:i * chunk]
        sys.stdout.write('\r' + color + BOLD + partial)
        sys.stdout.flush()
        time.sleep(0.055)
    sys.stdout.write('\r' + color + BOLD + text + RESET + '\n')


def print_divider(char: str = '─', width: int = 62, color: str = DIM + MIST_WHITE):
    print(color + char * width + RESET)


def print_header(title: str, artist: str, theme: str = 'gradient'):
    left, right = THEME_DECO.get(theme, (NOTE2, NOTE))
    palette = THEMES.get(theme, THEMES['gradient'])
    accent = palette[0]
    clear_screen()
    print()
    print_divider('═', color=accent + BOLD)
    print(accent + BOLD + center_text(f'{left}  {title}  {right}') + RESET)
    print(MIST_WHITE + DIM  + center_text(f'— {artist} —') + RESET)
    print_divider('═', color=accent + BOLD)
    print()


def print_section_label(label: str, theme: str = 'gradient'):
    """Print a chorus/verse/bridge section label."""
    palette = THEMES.get(theme, THEMES['gradient'])
    color = palette[1]
    left, right = THEME_DECO.get(theme, (NOTE2, NOTE))
    print(color + DIM + center_text(f'[ {left} {label} {right} ]') + RESET)
    time.sleep(0.3)


def print_lyrics(
    lines: list,
    style: str = 'gradient',
    line_delay: float = 1.2,
    theme: str = 'gradient',
    heart_chorus: bool = True,
):
    """
    Print lyrics beautifully.

    styles:
      - 'gradient'  : gradient color cycling (default)
      - 'typing'    : typewriter character-by-character
      - 'fade'      : fade-in per line
      - 'static'    : clean single color

    heart_chorus: if True, wraps lines starting with a # tag as section labels.
      Use  #Chorus  or  #Verse 1  as the first word of a line.
    """
    palette = THEMES.get(theme, THEMES['gradient'])
    color_index = 0

    for line in lines:
        stripped = line.strip()

        if not stripped:
            print()
            time.sleep(0.4)
            continue

        # Section tag: lines like "#Chorus" or "#Verse 1"
        if heart_chorus and stripped.startswith('#'):
            print_section_label(stripped[1:].strip(), theme=theme)
            print()
            continue

        color = palette[color_index % len(palette)]
        color_index += 1
        centered = center_text(stripped)

        if style == 'typing':
            typing_effect(centered, color=color, delay=0.03)
        elif style == 'fade':
            fade_in_line(centered, color=color)
        elif style == 'static':
            print(MIST_WHITE + BOLD + centered + RESET)
        else:
            print(color + BOLD + centered + RESET)

        time.sleep(line_delay)


def print_footer(theme: str = 'gradient'):
    palette = THEMES.get(theme, THEMES['gradient'])
    left, right = THEME_DECO.get(theme, (NOTE2, NOTE))
    accent = palette[-1]
    print()
    print_divider('─', color=DIM + accent)
    print(DIM + accent + center_text(f'{left}  {right}  {left}  {right}  {left}') + RESET)
    print(DIM + MIST_WHITE + center_text('end of lyrics') + RESET)
    print_divider('─', color=DIM + accent)
    print()


# ─── Demo: Rag Rag ───────────────────────────────────────────────────────────

SONG_TITLE  = 'Rag Rag'
SONG_ARTIST = 'Gajendra Verma'
THEME       = 'romantic'

LYRICS = """
#Verse 1
Rag rag woh samaya mere...
Rag Rag

Rag rag woh samaya mere...

#Verse 2
Har pal tujhe hi dhundhta hoon main
Khoyaa sa rehta hoon
Yaad teri dil mein basi hai
Tujhse judaa na rehna

#Chorus
Rag rag woh samaya mere...
Rag Rag
"""


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='gradient', line_delay=1.0, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
