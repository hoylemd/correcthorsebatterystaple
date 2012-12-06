import random
from math import floor

# load the wordlist
list_file = open('/usr/share/dict/words', 'r')
word_list = []
word = list_file.readline()
word_count = 1
while (word != ""):
  word_list.append(word)
  word_count += 1
  word = list_file.readline()

password = ""

for i in range(0, 4):
  word = random.choice(word_list).replace("\n", "").lower()
  password += word[0:1].upper() + word[1:]
  

print password

