"""
Sad Song Template
─────────────────────────────────────────────────────
Theme: 'sad'   — soul purple + sky blue + soft lilac
Style: 'typing' — typewriter feel, character by character
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lyrics_printer import print_header, print_lyrics, print_footer

SONG_TITLE  = 'Your Sad Song'
SONG_ARTIST = 'Artist Name'
THEME       = 'sad'

LYRICS = """
#Verse 1
[Paste verse 1 here]

#Chorus
[Paste chorus here]

#Verse 2
[Paste verse 2 here]

#Chorus
[Paste chorus here]

#Outro
[Paste outro here]
"""


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='typing', line_delay=1.3, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
