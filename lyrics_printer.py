import time
import sys
import os
import random

# ─── ANSI Color Palette ─────────────────────────────────────────────────────
DEEP_RED    = '\033[38;5;88m'
SOUL_PURPLE = '\033[38;5;54m'
WARM_GOLD   = '\033[38;5;136m'
MIST_WHITE  = '\033[38;5;251m'
ROSE_PINK   = '\033[38;5;211m'
SKY_BLUE    = '\033[38;5;75m'
SAGE_GREEN  = '\033[38;5;65m'
DUSK_ORANGE = '\033[38;5;172m'

BOLD   = '\033[1m'
DIM    = '\033[2m'
ITALIC = '\033[3m'
RESET  = '\033[0m'

# Gradient palette for cycling through lines
GRADIENT_COLORS = [DEEP_RED, SOUL_PURPLE, WARM_GOLD, ROSE_PINK, SKY_BLUE, DUSK_ORANGE]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def center_text(text: str, width: int = 60) -> str:
    """Return text centered within a given width."""
    return text.center(width)


def typing_effect(text: str, color: str = MIST_WHITE, delay: float = 0.04):
    """Print text character by character for a typewriter effect."""
    sys.stdout.write(color + BOLD)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + '\n')


def fade_in_line(text: str, color: str = MIST_WHITE, steps: int = 5):
    """Simulate a simple fade-in by printing progressively."""
    chunk = max(1, len(text) // steps)
    for i in range(1, steps + 1):
        partial = text[:i * chunk]
        sys.stdout.write('\r' + color + BOLD + partial)
        sys.stdout.flush()
        time.sleep(0.06)
    # print full line clean
    sys.stdout.write('\r' + color + BOLD + text + RESET + '\n')


def print_divider(char: str = '─', width: int = 60, color: str = DIM + MIST_WHITE):
    print(color + char * width + RESET)


def print_header(title: str, artist: str):
    clear_screen()
    print_divider('═', color=WARM_GOLD + BOLD)
    print(WARM_GOLD + BOLD + center_text(f'♪  {title}  ♪') + RESET)
    print(MIST_WHITE + DIM + center_text(f'— {artist} —') + RESET)
    print_divider('═', color=WARM_GOLD + BOLD)
    print()


def print_lyrics(lines: list, style: str = 'gradient', line_delay: float = 1.2):
    """
    Print lyrics beautifully.

    styles:
      - 'gradient'  : cycles through gradient colors
      - 'typing'    : typewriter effect
      - 'fade'      : fade-in per line
      - 'static'    : single color, clean
    """
    color_index = 0

    for line in lines:
        stripped = line.strip()

        # Blank lines = brief pause
        if not stripped:
            print()
            time.sleep(0.4)
            continue

        color = GRADIENT_COLORS[color_index % len(GRADIENT_COLORS)]
        color_index += 1

        centered = center_text(stripped)

        if style == 'typing':
            typing_effect(centered, color=color, delay=0.03)
        elif style == 'fade':
            fade_in_line(centered, color=color)
        elif style == 'static':
            print(MIST_WHITE + BOLD + centered + RESET)
        else:  # gradient (default)
            print(color + BOLD + centered + RESET)

        time.sleep(line_delay)


def print_footer():
    print()
    print_divider('─', color=DIM + SOUL_PURPLE)
    print(DIM + MIST_WHITE + center_text('♫  end of lyrics  ♫') + RESET)
    print_divider('─', color=DIM + SOUL_PURPLE)
    print()


# ─── Sample Song ─────────────────────────────────────────────────────────────

SONG_TITLE  = "Rag Rag"
SONG_ARTIST = "Gajendra Verma"

LYRICS = """
Rag rag woh samaya mere...
Rag Rag

Rag rag woh samaya mere...

Har pal tujhe hi dhundhta hoon main
Khoyaa sa rehta hoon
Yaad teri dil mein basi hai
Tujhse judaa na rehna

Rag rag woh samaya mere...
Rag Rag
"""


def main():
    lines = LYRICS.strip().split('\n')

    print_header(SONG_TITLE, SONG_ARTIST)

    # Choose style: 'gradient', 'typing', 'fade', or 'static'
    print_lyrics(lines, style='gradient', line_delay=1.0)

    print_footer()


if __name__ == '__main__':
    main()
