from getpass import _raw_input


def computepay(hrs, rate):
    if hrs > 40:
        gross_pay = (40 * rate) + ((hrs - 40) * rate * 1.5)
    else:
        gross_pay = 40 * rate
    return gross_pay

h = float(_raw_input("Enter hours: "))
r = float(_raw_input("Enter rate:"))
pay = computepay(h, r)
print(pay)

