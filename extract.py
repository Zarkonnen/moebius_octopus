from collections import defaultdict


with open('mobydick.txt') as f:
    mdick = f.read()

mdick = mdick.replace('\n', ' ').replace('--', ' ')
import re
p = re.compile('[ 0-9A-Za-z\'-]')

words = "".join([l for l in mdick if p.match(l)])

mergespaces = re.compile(' +')
words = mergespaces.sub(' ', words).lower()

counts = defaultdict(int)

for word in words.split(" "):
    counts[word] += 1

for k, v in sorted(counts.iteritems(), key=lambda i: -i[1]):
    print str(v) + "," + k + "," + k
