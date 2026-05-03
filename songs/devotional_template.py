"""
Devotional / Bhajan Template
─────────────────────────────────────────────────────
Theme: 'devotional' — warm gold + dusk orange + rose pink
Style: 'fade'       — soft, reverent line reveal
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lyrics_printer import print_header, print_lyrics, print_footer

SONG_TITLE  = 'Your Bhajan'
SONG_ARTIST = 'Artist Name'
THEME       = 'devotional'

LYRICS = """
#Stanza 1
[Paste stanza 1 here]

#Refrain
[Paste refrain here]

#Stanza 2
[Paste stanza 2 here]

#Refrain
[Paste refrain here]
"""


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='fade', line_delay=1.4, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
