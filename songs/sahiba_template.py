"""
Sahiba — by Aditya Rikhari
─────────────────────────────────────────────────────
This is a ready-to-use template.
Paste the lyrics you have from any licensed source
into the LYRICS string below, then run:

    python songs/sahiba_template.py

Theme: 'romantic'  — rose pink + soul purple + warm gold
Style: 'fade'      — lines slide in softly
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lyrics_printer import print_header, print_lyrics, print_footer

SONG_TITLE  = 'Sahiba'
SONG_ARTIST = 'Aditya Rikhari'
THEME       = 'romantic'

# ── Paste your own lyrics here ──────────────────────────────────────────────
# Use  #Chorus ,  #Verse 1 ,  #Bridge  etc. as section markers.
# Leave a blank line between sections for a natural pause.
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
# ─────────────────────────────────────────────────────────────────────────────


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='fade', line_delay=1.1, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
