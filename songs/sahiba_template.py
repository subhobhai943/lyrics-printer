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
#Verse 1 ~4.0
Sahiba, aaye ghar kaahe na ~3.5
Aise toh sataye na ~3.0
Dekhun tujhko chain aata hai ~4.0
Sahiba, neende-veende aaye na ~3.5
Raatein kaati jaaye na ~3.0
Tera hi khayal din-rain aata hai ~5.0

#Chorus ~3.0
Sahiba, samundar, meri aankhon mein reh gaye ~3.5
Hum aate-aate jaana, teri yaadon mein reh gaye ~3.5
Ye palke gawaahi hai, hum raaton mein reh gaye ~3.5
Jo vaade kiye saare, bas baaton mein reh gaye ~5.0

#Verse 2 ~3.5
Baaton-baaton mein hi, khwabon-khwabon mein hi mere qareeb hai tu ~4.0
Teri talab mujhko, teri talab, jaana, ho tu kabhi rubaru ~4.0
Shor-sharaaba, baaba, jo seene mein hai mere ~3.5
Kaise bayaan main karun ~3.0
Haal jo mera hai, main kisko bataun ~3.5
Mere Sahiba! ~5.0

#Verse 3 ~3.5
Dil na kiraye ka, thoda toh sambhalo na ~3.5
Naazuk hai yeh, toot jaata hai ~3.5
Sahiba, neende-veende aaye na ~3.5
Raatein kaati jaaye na ~3.0
Tera hi khayal din-rain aata hai ~5.0

#Bridge ~4.0
Kaisi bhala, shab hogi woh ~4.0
Sang jo tere, dhalti hai ~3.5
Dil ko koi, khwahish nahi ~3.5
Teri kami, jaana, khalti hai ~4.5

Aaraam na ab aankhon ko ~4.0
Khwaab bhi na badalte hain ~3.5
Dil ko koi, chaahat nahi ~3.5
Teri kami, jaana, khalti hai ~5.0

#Outro ~4.0
Sahiba, tu hi mera aayina ~3.5
Haathon mein bhi mere, haan ~3.0
Tera hi naseeb aata hai ~4.5

Sahiba, neende-veende aaye na ~3.5
Raatein kaati jaaye na ~3.0
Tera hi khayal din-rain aata hai ~4.0
Sahiba, neende-veende aaye na ~3.5
Raatein kaati jaaye na ~4.0
"""
# ─────────────────────────────────────────────────────────────────────────────


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='fade', line_delay=3.0, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
