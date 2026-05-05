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
Sahiba, aaye ghar kaahe na
Aise toh sataye na
Dekhun tujhko chain aata hai
Sahiba, neende-veende aaye na
Raatein kaati jaaye na
Tera hi khayal din-rain aata hai

#Chorus
Sahiba, samundar, meri aankhon mein reh gaye
Hum aate-aate jaana, teri yaadon mein reh gaye
Ye palke gawaahi hai, hum raaton mein reh gaye
Jo vaade kiye saare, bas baaton mein reh gaye

#Verse 2
Baaton-baaton mein hi, khwabon-khwabon mein hi mere qareeb hai tu
Teri talab mujhko, teri talab, jaana, ho tu kabhi rubaru
Shor-sharaaba, baaba, jo seene mein hai mere
Kaise bayaan main karun
Haal jo mera hai, main kisko bataun
Mere Sahiba!

#Verse 3
Dil na kiraye ka, thoda toh sambhalo na
Naazuk hai yeh, toot jaata hai
Sahiba, neende-veende aaye na
Raatein kaati jaaye na
Tera hi khayal din-rain aata hai

#Bridge
Kaisi bhala, shab hogi woh
Sang jo tere, dhalti hai
Dil ko koi, khwahish nahi
Teri kami, jaana, khalti hai

Aaraam na ab aankhon ko
Khwaab bhi na badalte hain
Dil ko koi, chaahat nahi
Teri kami, jaana, khalti hai

#Outro
Sahiba, tu hi mera aayina
Haathon mein bhi mere, haan
Tera hi naseeb aata hai

Sahiba, neende-veende aaye na
Raatein kaati jaaye na
Tera hi khayal din-rain aata hai
Sahiba, neende-veende aaye na
Raatein kaati jaaye na
"""
# ─────────────────────────────────────────────────────────────────────────────


def main():
    lines = LYRICS.strip().split('\n')
    print_header(SONG_TITLE, SONG_ARTIST, theme=THEME)
    print_lyrics(lines, style='fade', line_delay=1.1, theme=THEME)
    print_footer(theme=THEME)


if __name__ == '__main__':
    main()
