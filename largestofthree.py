
number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
number3 = int(input("Enter the third integer: "))
if number1 >= number2:
    if number1 >= number3:
        largest = number1
    else:
        largest = number3
else:
    if number2 >= number3:
        largest = number2
    else:
        largest = number3
print("The largest number is:", largest)