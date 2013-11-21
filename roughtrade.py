
from bs4 import BeautifulSoup
import requests

from helpers import to_csv


def main():
    r = requests.get('http://thelineofbestfit.com/news/latest-news/rough-trade-unveil-albums-of-the-year-list-for-2013-141558')
    soup = BeautifulSoup(r.text, 'lxml')
    lines = soup.find_all('p')[5].get_text().split("\n")
    results = []
    for line in lines:
        pieces = line.split(' ')
        if not pieces[0]:
            continue
        if pieces[0] == '(Joint)':
            pieces = pieces[1:]
        num = int(pieces[0].replace('(Joint)', '').replace('.', ''))
        pieces = pieces[1:]
        if num == 22:
            artist = u'Public Service Broadcasting'
            album = u'Inform - Educate - Entertain'
        elif u'\u2013' in pieces:
            i = pieces.index(u'\u2013')
            artist = u' '.join(pieces[0:i])
            album = u' '.join(pieces[i+1:])
        else:
            for i, piece in enumerate(pieces):
                if piece.startswith(u'-\xa0'):
                    artist = u' '.join(pieces[0:i])
                    pieces[i] = piece.replace(u'-\xa0', u'')
                    album = u' '.join(pieces[i:])
                    break
                if piece.startswith(u'-'):
                    artist = u' '.join(pieces[0:i])
                    pieces[i] = piece.replace(u'-', u'')
                    album = u' '.join(pieces[i:])
                    break
        album = album.replace(u'\u2019', u'').replace(u'\u2026.', '...').replace(u'\u2026', '... ')
        results.append([num, artist, album])
        #print "%s. %s - %s" % (num, artist, album)
    to_csv(results, __file__)


if __name__ == '__main__':
    main()
