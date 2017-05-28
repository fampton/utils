#!/usr/bin/env python
import boto
from dateutil.relativedelta import *
from datetime import *
from dateutil.parser import parse

conn=boto.connect_s3()
bob=conn.get_bucket('bob')
list=bob.list(prefix='auto')

TODAY = date.today()
monthago = TODAY+relativedelta(months=-1)
weekago = TODAY+relativedelta(days=-7)

def get_recent():
  myshows = []
  for i in list:
    if parse(i.last_modified).date() > monthago:
      myshows.append('http://bobp.fanp.co/bob/'+i.name)
  return myshows

def get_week():
  myshows = []
  for i in list:
    if parse(i.last_modified).date() > weekago:
      myshows.append('http://bobp.fanp.co/bob/'+i.name)
  return myshows

def get_week_string():
  mystring = ''
  for i in list:
    if parse(i.last_modified).date() > weekago:
      mystring = mystring + 'http://bobp.fanp.co/bob/'+i.name+'\n'
  return mystring

if __name__ == "__main__":
  recent=get_recent()
  for i in recent:
    print i

