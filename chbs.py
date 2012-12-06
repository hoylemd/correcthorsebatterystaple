import random
print ''.join([random.choice(open('/usr/share/dict/words','r').readlines()).strip().title() for i in range(4)])
