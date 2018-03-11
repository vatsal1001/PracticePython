number = int(input('Enter a number: '))
divisors = [x for x in range(1, number//2 + 1) if(number % x == 0)]
divisors = str(divisors)[1:-1]
print('The divisors are: ', divisors)