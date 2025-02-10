hours= input('Enter Hours: ')
try:
    hours=float (hours)
except:
    print('Error, please enter numeric input')
    quit()
rate= input ('Enter rate: ')
try:
    rate=float(rate)
except:
    print('Error, please enter numeric input')
    quit()
if hours>40:
    xp=40*rate + ((hours-40)*(1.5*rate))
else:
    xp=hours*rate
print('Pay: ',xp)