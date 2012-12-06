import random
l = open('/usr/share/dict/words', 'r').readlines()
p = ""
for i in range(0, 4):
  w = random.choice(l).replace("\n", "")
  p += w.title()
print p

