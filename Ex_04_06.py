hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter Rate:')
r = float(rate)
def computepay(h,r):

    if h > 40:

        reg_pay = h * r

        ot_pay = (h-40) * (r * 0.5)

        pay = reg_pay + ot_pay

    else:

        pay = h * r

    return pay
pay = computepay(h, r)
p = pay
print("Pay", p)