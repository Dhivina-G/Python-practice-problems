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

elements = (1,4,3,12,2,66)
k = int(input('Enter the number of values to check:'))
elements_sorted = sorted(elements)                         # sort the elements
min_values = elements_sorted[:k]                           # using slice get first k elements
max_values = elements_sorted[-k:]                          # using slice get last k elements
print(f'minimum values:{min_values}')
print(f'maximum values:{max_values}')

# 28. Create a list of tuples from given list having number and its cube in each tuple

numbers = [1,2,3,4,5]
new_list = []                          # create an empty list 
for number in numbers:
    tuple_value = (number,number**3)   # a tuple with number and cube
    new_list.append(tuple_value)       # append each tuple to list
print(new_list)

# 29. Python – Adding Tuple to List and vice – versa

items = ('book','pen','bottle','shoe')
items_list = [3,12,1]                     # created a list   
items_list.append(items)                  # append the tuple items to list
print(items_list)

items_tuple = (2,14,33)  
items = ['book','pen','bottle','shoe']
items_list = list(items_tuple)             # convert tuple to list
items_list.append(items)                   # append items to the converted tuple
items_tuple = tuple(items_list)            # again change the list to tuple
print(items_tuple)

# 30. Python – Closest Pair to Kth index element in Tuple

elements = (1,4,5,6,2)
k = int(input('Enter the index of element:'))
k_value = elements[k]                                     # index value of k
for num in range(len(elements)):                          # iterate from first value
    for nums in range(num+1,len(elements)):               # iterate from second value
        if(elements[num]+elements[nums]==k_value):        # check if the sum is equal to k_value
            print(f'{elements[num]},{elements[nums]}')
            break
          



        