"""
Romantic Song Template
─────────────────────────────────────────────────────
Theme: 'romantic' — rose pink + deep red + warm gold
Style: 'gradient' — each line in a different warm color
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lyrics_printer import print_header, print_lyrics, print_footer

SONG_TITLE  = 'Your Romantic Song'
SONG_ARTIST = 'Artist Name'
THEME       = 'romantic'

LYRICS = """
#Verse 1
[Paste verse 1 here]

#Chorus
[Paste chorus here]

#Verse 2
[Paste verse 2 here]

#Chorus
[Paste chorus here]

#Bridge
[Paste bridge here]
"""


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='gradient', line_delay=1.0, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
