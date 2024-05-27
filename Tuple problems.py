# 26. Python program to Find the size of a Tuple

number = (2,3,4,1,12,99)
length = len(number)
print(length)

numbers = (2,3,4,1,12,99)
count = 0
for number in numbers:
    count += 1
print(count)

# 27. Python – Maximum and Minimum K elements in Tuple

# 28. Create a list of tuples from given list having number and its cube in each tuple

numbers = [1,2,3,4,5]
new_list = []                          # create an empty list 
for number in numbers:
    tuple_value = (number,number**3)   # a tuple with number and cube
    new_list.append(tuple_value)       # append each tuple to list
print(new_list)

# 29. Python – Adding Tuple to List and vice – versa

items = ('book','pen','bottle','shoe')
items_list = list(items)                 # list() to convert tuple to list
print(items_list)

items = ['book','pen','bottle','shoe']
items_tuple = tuple(items)              # tuple() to convert tuple to list
print(items_tuple)

# 30. Python – Closest Pair to Kth index element in Tuple
