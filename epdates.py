#!/usr/bin/env python
import requests
import sys
from bs4 import BeautifulSoup

epget = requests.get('http://epguides.com/{}'.format(sys.argv[1]))
soup = BeautifulSoup(epget.content, 'lxml')
eplist = soup.body.find('div', id='eplist')
for episode in str(eplist).splitlines():
    if 'href' in episode:
        if len(sys.argv) > 2:
          if episode.split()[1].startswith(sys.argv[2]):
            print episode.split()[1:5]
        else:
          print episode.split()[1:5]
