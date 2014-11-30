from collections import defaultdict
import re

with open('mobydick.txt') as f:
    mdick = f.read()

repl = {}

with open('replacements.csv') as f:
    for l in f:
        try:
            n, old, new = l[:-1].split(",")
            if old != new:
                repl[old] = new
        except:
            pass

startindex = 0

wordfinder = re.compile('[a-zA-Z0-9\']+-?[a-zA-Z0-9\']*')

while True:
    match = wordfinder.search(mdick, startindex)
    if not match:
        break
    old = match.group()
    if old.lower() in repl:
        new = repl[old.lower()]
        if all(l.isupper() for l in old):
            new = new.upper()
        elif old[0].isupper():
            new = new.capitalize()
        else:
            new = new.lower()
        mdick = mdick[:match.start()] + new + mdick[match.end():]
        startindex = match.end() - len(old) + len(new)
    else:
        startindex = match.end()

print mdick
