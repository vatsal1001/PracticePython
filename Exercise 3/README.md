# Exercise 3
Work with lists and conditionals in this one. Use a concept known as list comprehension. What this essentially is is a way of working in lists in a more compact form, and reduces the extra lines of code which would otherwise have been used for something basic.

For example, if you want to create a new list with only the even numbers from the original list, this is the code you could use:   
```
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [item for item in original_list if item % 2 == 0]
```
Now, `new_list` will only have the even numbers from `original_list`
