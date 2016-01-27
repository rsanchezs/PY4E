from getpass import _raw_input

largest = None
smallest = None

while True:
    num = _raw_input("Enter a number: ")
    if num == "done":
        break
    try:
        if largest == None and smallest == None:
            largest = int(num)
            smallest = int(num)
        elif int(num) < smallest:
            smallest = num
        else:
            largest = num
    except:
     print("Invalid input")

print("Maximum is:", smallest)
print("Minimum is:", largest)
