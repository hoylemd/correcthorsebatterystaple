#!/bin/python

#correcthorsebatterystaple
#=========================

#password generator

#uses the wordlist found at /usr/share/dict/words

#generates a camel-cased password of 4 random words from that list

import random
import contextlib

with contextlib.closing(open('/usr/share/dict/words', 'r')) as f:
	word_list = f.readlines()

password = ""
for i in range(4):
	password += random.choice(word_list).strip().title()

print password
