from getpass import _raw_input
from builtins import print

fname = _raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst = list()
for line in fh:
    line.rstrip()
    if line.startswith("From:"):
        lst = line.split()
        print (lst[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
