import random, sys
l=open('/usr/share/dict/words','r').readlines()
for i in range(0,4): sys.stdout.write(random.choice(l).replace("\n", "").title())
sys.stdout.write("\n")
