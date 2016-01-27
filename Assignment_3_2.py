from getpass import _raw_input

from builtins import print

score = float(_raw_input("Enter a score:"))
if score < 0.0 or score > 1.0:
    print("The entered value is out of range")
    print("Exiting of the program...")
    quit()
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print ("B")
elif score >= 0.7:
    print ("C")
elif score >= 0.6:
    print ("D")
elif score < 0.6:
    print ("F")



