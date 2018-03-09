import datetime
name = input('Enter your name: ')
age = int(input('Enter your age: '))
copies = int(input('Enter number of copies: '))
yearAt100 = datetime.datetime.now().year + 100 - age
print(("Hey " + name + ", you will turn 100 in the year " + str(yearAt100) + "\n") * copies)