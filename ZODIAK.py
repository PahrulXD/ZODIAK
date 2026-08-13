import os
import sys
from datetime import date

# Otomatis install modul jika belum ada
try:
    import requests
    from bs4 import BeautifulSoup as bs
except ImportError:
    print("Menginstal modul yang dibutuhkan...")
    os.system('pip install --upgrade requests beautifulsoup4')
    import requests
    from bs4 import BeautifulSoup as bs


def get_zodiac_map():
    return {
        '01': ('aries', 1), '02': ('taurus', 2), '03': ('gemini', 3), '04': ('cancer', 4),
        '05': ('leo', 5), '06': ('virgo', 6), '07': ('libra', 7), '08': ('scorpio', 8),
        '09': ('sagittarius', 9), '10': ('capricorn', 10), '11': ('aquarius', 11), '12': ('pisces', 12)
    }



def main_menu():
    zodiak = ('''\033[1;91m
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣿⣿⣿⣷⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡏⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠉⣿⣿
⢻⣿⡇⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⢀⣿⡇
⠘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⢀⣼⣿⠃
⠀⠹⣿⣿⣶⣦⣤⣀⣀⣀⣀⣀⣤⣶⠟⡿⣷⣦⣄⣀⣀⣀⣠⣤⣤⣶⣿⣿⡟⠀
⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⢈⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣷⠀⣼⣷⠀⣸⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⡇⠀
⠀⠘⣿⣿⣿⡟⠋⠀⠀⠰⣿⣿⣿⣷⣿⣿⣷⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⠟⠁⠀
⠀⠀⠈⠉⠀⠈⠁⠀⠀⠘⣿⣿⢿⣿⣿⢻⣿⡏⣻⣿⣿⠃⠀⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⠃⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⣿⣿⢸⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠇⢿⡿⢸⡿⠀⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

\033[1;94m- Coding By : Pahrul Aguspriana XF.
\033[1;94m- Version  : 0.1
\033[1;91m
[01] Aries  [06] Virgo   [11] Aquarius                [02] Taurus [07] Libra   [12] Pisces
[03] Gemini [08] Scorpio                              [04] Cancer [09] Sagittarius
[05] Leo    [10] Capricorn
''')
    print(zodiak)
    choice = input("\033[1;91m- pilih : ").lower()
    if choice == 'x': sys.exit()
    return get_zodiac_map().get(choice)

def fetch_prediction(zodiac_name, zodiac_id):
    url = f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={zodiac_id}'
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10)'}
        res = requests.get(url, headers=headers, timeout=10)
        soup = bs(res.text, 'html.parser')
        content = soup.find('main').find('p').text.strip()
        print(f"\n\033[1;92m{content}")
    except Exception as e:
        exit()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    
    zodiac = main_menu()
    if zodiac:
        fetch_prediction(zodiac[0], zodiac[1])
    else:
        exit()