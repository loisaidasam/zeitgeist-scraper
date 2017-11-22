zeitgeist-scraper
=================

A collection of year-end music lists from across the blogosphere. Feel free to contribute!

The language or methodology for these scrapers isn't as important as the end result. I'd like to have a collection of .csv files with three columns: #, artist name, and album name. If a blog has a tie for two albums, that's fine, just use the same # for both.

Hopefully once we have all of the data, someone (or myself) can put together a website that displays them all in one common easy-to-read format.

Update: I found this site

[http://www.albumoftheyear.org](http://www.albumoftheyear.org)

and it kinda does everything I was looking to do [here](http://www.albumoftheyear.org/lists.php) ...

A fun tip though, if you want to get the raw text lists from any of these, choose a list, such as NPR, and use the link in combination with [pup](https://github.com/EricChiang/pup) like this:

    curl -s http://www.albumoftheyear.org/list/340-npr-musics-50-favorite-albums-of-2014/ | pup '.post-title a text{}'

Happy AOTY'ing :)
