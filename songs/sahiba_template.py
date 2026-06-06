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

# ── Lyrics with per-line timing synced to official track ─────────────────────
# Timings derived from LRC sync by Adarsh272010 (megalobiz.com)
# Song duration: 3:03  |  BPM: 100  |  Key: A# Minor
#
# ~X.X = seconds to pause AFTER displaying this line
# Delay = (start time of next line) − (start time of this line)
#
# LRC timestamps used:
#   00:12.38  Sahiba Aaye Ghar Kaahe Na
#   00:15.85  Aise Toh Sataye Na
#   00:18.76  Dekhun Tujhko Chain Aata Hai
#   00:22.21  Sahiba Neende Veende Aaye Na
#   00:25.67  Raatein Kaati Jaaye Na
#   00:28.32  Tera Hi Khayal Din Rain Aata Hai
#   00:32.84  Sahiba Samundar Meri Aankhon Mein Reh Gaye
#   00:37.35  Hum Aate Aate Jaana Teri Yaadon Mein Reh Gaye
#   00:42.68  Yeh Palkein Gawahi Hai Hum Raaton Mein Reh Gaye
#   00:47.73  Jo Wade Kiye Sare Bas Baaton Mein Reh Gaye
#   00:51.46  Baaton Baaton Mein Hi Khwabon Khwabon Mein Hi Mere Kareeb Hai Tu
#   00:54.40  Teri Talab Mujhko Teri Talab Jaana Ho Tu Kabhi Rubaroo
#   00:57.85  Shor Sharaba Jo Seene Mein Hai Mere
#   01:01.57  Kaise Bayaan Main Karun
#   01:05.56  Haal Jo Mera Hai Main Kis Ko Bataun
#   01:09.81  Mere Sahiba!
#   01:09.81  Dil Na Kiraye Ka Thoda Toh Sambhalo Na  (same breath)
#   01:13.26  Thoda Toh Sambhalo Na
#   01:16.71  Nazuk Hai Yeh Toot Jata Hai
#   01:20.43  Sahiba Neendein Veendein Aaye Na
#   01:23.64  Raatein Kaati Jaayein Na
#   01:25.76  Tera Hi Khayal Din Rain Aata Hai
#   -- instrumental break --
#   01:44.09  Kaisi Bhala Shab Hogi Wo
#   01:48.61  Sang Jo Tere Dhalti Hai
#   01:53.39  Dil Ko Koi Khwahish Nahi
#   01:57.91  Teri Kami Khalti Hai
#   02:03.21  Aaram Na Ab Aankhon Ko
#   02:07.46  Khwaab Bhi Na Badalti Hai
#   02:12.77  Dil Ko Koi Khwahish Nahi
#   02:17.29  Teri Kami Jana Khalti Hai
#   02:22.34  Sahiba Tu Hi Mera Aina
#   02:23.93  Hathon Mein Bhi Mere Haan
#   02:28.19  Tera Hi Naseeb Aata Hai
#   02:32.17  Sahiba Neende-Veende Aaye Na
#   02:35.36  Raatein Kaati Jaayein Na
#   02:37.48  Tera Hi Khayal Din Rain Aata Hai
#   02:41.46  Sahiba Neende-Veende Aayein Na
#   02:44.39  Raatein Kaati Jaaye Na
#   02:47.04  (end of vocal)
# ─────────────────────────────────────────────────────────────────────────────
LYRICS = """
#Verse 1 ~3.0
Sahiba, aaye ghar kaahe na ~3.5
Aise toh sataye na ~2.9
Dekhun tujhko chain aata hai ~3.5
Sahiba, neende-veende aaye na ~3.5
Raatein kaati jaaye na ~2.7
Tera hi khayal din-rain aata hai ~4.5

#Chorus ~2.0
Sahiba, samundar, meri aankhon mein reh gaye ~4.5
Hum aate-aate jaana, teri yaadon mein reh gaye ~5.3
Ye palke gawaahi hai, hum raaton mein reh gaye ~5.1
Jo vaade kiye saare, bas baaton mein reh gaye ~3.7

#Verse 2 ~1.5
Baaton-baaton mein hi, khwabon-khwabon mein hi mere qareeb hai tu ~2.9
Teri talab mujhko, teri talab, jaana, ho tu kabhi rubaru ~3.5
Shor-sharaaba, baaba, jo seene mein hai mere ~3.7
Kaise bayaan main karun ~4.0
Haal jo mera hai, main kisko bataun ~4.3
Mere Sahiba! ~0.5
Shor-sharaaba, baaba, jo seene mein hai mere ~3.5

#Verse 3 ~1.5
Dil na kiraye ka, thoda toh sambhalo na ~3.5
Naazuk hai yeh, toot jaata hai ~3.7
Sahiba, neende-veende aaye na ~3.2
Raatein kaati jaaye na ~2.1
Tera hi khayal din-rain aata hai ~18.3

#Bridge ~2.0
Kaisi bhala, shab hogi woh ~4.5
Sang jo tere, dhalti hai ~4.8
Dil ko koi, khwahish nahi ~4.5
Teri kami, jaana, khalti hai ~5.3

Aaraam na ab aankhon ko ~4.3
Khwaab bhi na badalte hain ~5.3
Dil ko koi, chaahat nahi ~4.5
Teri kami, jaana, khalti hai ~5.1

#Outro ~2.0
Sahiba, tu hi mera aayina ~1.6
Haathon mein bhi mere, haan ~4.3
Tera hi naseeb aata hai ~4.0

Sahiba, neende-veende aaye na ~3.2
Raatein kaati jaaye na ~2.1
Tera hi khayal din-rain aata hai ~4.0
Sahiba, neende-veende aaye na ~2.9
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
