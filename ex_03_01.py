hrs = float(input('Enter hours: '))
rate = float(input('Enter rate per hour: '))
pay = hrs * rate

if hrs > 40:
    above_40 = hrs - 40
    pay = 40 * rate + above_40 *  rate * 1.5
    print("Overtime")
else:
    print("regular")

print(pay)