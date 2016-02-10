from getpass import _raw_input
from builtins import print

name = _raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line.rstrip()
    if not line.startswith("From"): continue
    words = line.split()
    if words[0].endswith(":"): continue
    time = words[5]
    hour = time[:2]
    counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key, value in counts.items():
    lst.append((key, value))

lst.sort()
for key, value in lst:
    print (key, value)