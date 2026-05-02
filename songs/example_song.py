"""Example: Add your own song here."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lyrics_printer import (
    print_header, print_lyrics, print_footer
)

SONG_TITLE  = "Your Song Title"
SONG_ARTIST = "Artist Name"

LYRICS = """
First verse line one
First verse line two

Chorus line one
Chorus line two
Chorus line two again

Second verse line one
Second verse line two

Chorus line one
Chorus line two
"""

def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST)
    print_lyrics(lines, style='gradient', line_delay=1.0)
    print_footer()

if __name__ == '__main__':
    main()
