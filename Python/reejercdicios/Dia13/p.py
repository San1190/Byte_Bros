from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep


flag = 0
client_id = "af93b791b15a4b3983a275ca9e0f3a56"
client_secret = "09be25552e574621a3882d5f8f99cd37"
autor = '' 


song = input("").upper()





if len(autor) > 0:

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    result = sp.search(autor)

    for i in range(0, len(result["tracks"]["items"])):
        name_song = result["tracks"]["items"][i]["name"].upper()
        if song in name_song:
            flag = 1
            webbrowser.open(result["tracks"]["items"][i]["uri"])
            sleep(5)
            pyautogui.press("enter")

if flag == 0:
    song= song.replace(" ", "%20")
    webbrowser.open(f'spotify:search:{song}')
    sleep(3)
    for i in range(4):
        pyautogui.press("tab")  
    pyautogui.press("enter")



    