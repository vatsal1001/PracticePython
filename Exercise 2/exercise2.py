num = int(input('Enter your number: '))
check = int(input('Enter the divisor: '))
if (num % 4 == 0):
    print(str(num) + ' is divisible by 4')
elif (num % 2 == 0):
    print(str(num) + ' is an even number')
else:
    print(str(num) + ' is an odd number')
if (num % check == 0):
    print(str(check) + ' divides ' + str(num))
else:
    print(str(check) + ' does not divide ' + str(num))