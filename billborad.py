import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://ryukiwon:test@cluster0.kd1rkbx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

URL = "https://www.billboard-japan.com/charts/detail?a=hot100"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#content2 > div > div.leftBox > table > tbody > tr')

for a in musics:
    rank = a.select_one('td > span').text
    title = a.select_one('p.musuc_title').text.strip()
    artist = a.select_one('p.artist_name').text.strip()
    print(rank, title, artist)