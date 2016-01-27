from getpass import _raw_input

hrs = float(_raw_input("Enter hours: "))
rate = float(_raw_input("Enter rate:" ))
if hrs > 40:
    gross_pay = (40 * rate) + ((hrs - 40) * rate * 1.5)
else:
    gross_pay = 40 * rate
print(gross_pay)
