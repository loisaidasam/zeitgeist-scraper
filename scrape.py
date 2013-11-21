#!/usr/bin/env python

import sys


def main():
    if not len(sys.argv) > 1:
        # TODO: print scrapers available
        raise Exception("Specify scraper name")
    name = 'scrapers.%s' % sys.argv[1]
    scraper = __import__(name, fromlist=['scrape'])
    results = scraper.scrape()
    for result in results:
        num, artist, album = result
        print "#%s. %s - %s" % (num, artist, album)


if __name__ == '__main__':
    main()
