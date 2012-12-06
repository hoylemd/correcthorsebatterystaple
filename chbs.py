import random
import contextlib

with contextlib.closing(open('/usr/share/dict/words', 'r')) as f:
	word_list = f.readlines()

password = ""
for i in range(4):
	password += random.choice(word_list).strip().title()

print password	
