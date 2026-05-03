"""
Neon / Lo-Fi Song Template
─────────────────────────────────────────────────────
Theme: 'neon' — sky blue + mint + rose pink
Style: 'typing' — fast typewriter, chill vibe
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lyrics_printer import print_header, print_lyrics, print_footer

SONG_TITLE  = 'Your Lo-Fi Track'
SONG_ARTIST = 'Artist Name'
THEME       = 'neon'

LYRICS = """
#Hook
[Paste hook here]

#Verse 1
[Paste verse 1 here]

#Hook
[Paste hook here]

#Verse 2
[Paste verse 2 here]

#Outro
[Paste outro here]
"""


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='typing', line_delay=0.9, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
