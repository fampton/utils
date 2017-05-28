#!/usr/bin/env python

import requests
import sys
from bs4 import BeautifulSoup as bs

turl = sys.argv[1]
headers = {
        'Host': '{}'.format(turl),
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://{}/'.format(turl),
        'Connection': 'keep-alive'
        }


myreq = requests.get('https://{}/search/{}/0/99/0'.format(turl, sys.argv[2]), headers=headers)
mysoup = bs(myreq.content, 'html.parser')
tables = mysoup.findChildren('table')
my_table = tables[0]
rows = my_table.findChildren(['tr'])
for row in rows:
  try:
    title = row.findChildren('a', class_='detLink')[0].text
    magnet_cell = row.findChildren('td')[1]
    mymagnet = magnet_cell.findChildren('a')[1]
    size = row.findChildren('font', class_='detDesc')[0].text.split(',')[1]
    se, le = row.findChildren('td')[-2:]
    print title, "".join(mymagnet['href'].split('&')[0:2]),size,'SE',se.text,'LE',le.text
  except:
    pass
