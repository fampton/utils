#!/usr/bin/env python

import os
import sys 

from slacker import Slacker

token = os.environ['SLACK_API_TOKEN']
slack = Slacker(token)

def main(person, message):
    print person, message
    slack.chat.post_message(person, message)

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2])
