import requests , urllib.request
import os
import sys
import time
from bs4 import BeautifulSoup
blue = '\033[34;1m'
green = '\033[32;1m'
purple = '\033[35;1m'
cyan = '\033[36;1m'
red = '\033[31;1m'
white = '\033[37;1m'
yellow = '\033[33;1m'
session = requests.Session()
def main():
    url = "https://www.planetlagu.blog"
    konten = session.get(url)
    soup = BeautifulSoup(konten.content, "html.parser")
    angka = 0
    for lagu in soup.find_all("div", class_="media-body ktz-post"):
        angka += 1
        print (str(angka), lagu.text)

def link(x):
    url = "https://www.planetlagu.blog"
    konten = session.get(url)
    soup = BeautifulSoup(konten.content, "html.parser")
    angka = 0
    for lagu in soup.find_all("div", class_="media-body ktz-post"):
        angka += 1
        if angka == x:
           for jud in lagu.findChildren('a', rel="bookmark"):
               global link
               link = jud.get('href')
               global judul_lagu
               judul_lagu = lagu.text
               break

def Download_Progress(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def pilihan():
    main()
    pilihan = input('Masukkan Lagu : ')
    link(int(pilihan))
    konten = session.get(link)
    soup = BeautifulSoup(konten.content, "html.parser")
    for lagu in soup.find_all("div", class_="embed-audio-mp3"):
        for link1 in lagu.findChildren('source'):
            down = link1.get('src')
            urllib.request.urlretrieve(down, judul_lagu+'.mp3', reporthook=Download_Progress)

os.system(" figlet -f slant MR.CL4Y |lolcat")

if __name__ == "__main__":
     pilihan()
