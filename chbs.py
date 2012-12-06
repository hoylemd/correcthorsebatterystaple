import random
word_list = open('/usr/share/dict/words', 'r').readlines()
password = ""
for i in range(0, 4):
  word = random.choice(word_list).replace("\n", "").lower()
  password += word[0:1].upper() + word[1:]
print password

