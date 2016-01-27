from getpass import _raw_input
from builtins import print

name = _raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dictionary = dict()

for line in handle:
    line.rstrip()
    if not line.startswith("From:"): continue
    words = line.split()
    dictionary[words[1]] = dictionary.get(words[1], 0) + 1

senders_mail_address = None
count = None
for key, value in dictionary.items():
    if senders_mail_address is None or value > count:
        senders_mail_address = key
        count = value
print (senders_mail_address, count)