a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
newList = [item for item in a if item < 5]
print('List of items less than 5: ', newList)
cutoff = int(input('Enter the cutoff value: '))
newList = [item for item in a if item < cutoff]
print('List of items less than ', str(cutoff), ': ', newList)