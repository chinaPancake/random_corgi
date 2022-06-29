from pexels_api import API
from tkinter import *
import random
import webview


global link_check
link_check = open('corgilink.txt', 'a+', encoding='utf-8')

windows = Tk()
windows.geometry("1960x1080")

rpage = random.randint(1,350)

 #Getting api key from pexels
PEXELS_API_KEY = '563492ad6f917000010000018b2652bcf7e841a0b049109d310692e0'
api = API(PEXELS_API_KEY)

#Looking for 'corgi' 1 results per page, random page 1-350
api.search('corgi', page=rpage, results_per_page=1)
photos = api.get_entries()

for photo in photos:
    print('photographer: ', photo.photographer)
    print(photo.original)
    link_check.write(photo.original + '\n')
    if (photo.original in link_check.read()):
        print('Te zdjecie już było')
    else:
        print('To nowe zdjęcie')

webview.create_window('Corgi for Oliwia', photo.original)
webview.start()