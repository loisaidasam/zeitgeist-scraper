
from bs4 import BeautifulSoup
import requests

def scrape():
    r = requests.get('http://thelineofbestfit.com/news/latest-news/rough-trade-unveil-albums-of-the-year-list-for-2013-141558')
    soup = BeautifulSoup(r.text, 'lxml')
    lines = soup.find_all('p')[5].split("\n")
    results = []
    for line in lines:
        pieces = line.split(' ')
        num = pieces[0].replace(['(Joint)', '.'], ['', ''])
        artist = ''
        album = ''
        results.append([num, artist, album])
    return results
