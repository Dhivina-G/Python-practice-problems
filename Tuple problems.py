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
    for nums in range(num+1, len(elements)):               # iterate from second value
        if elements[num] + elements[nums] == k_value:        # check if the sum is equal to k_value
            print(f'{elements[num]},{elements[nums]}')
            break
          
#  ----------------27/4/24----------------------------

# Python – Join Tuples if similar initial element

first_elements = (1,3,41,13,77)
second_elements = (2,6,35,71,1)
first_ele = first_elements[0]
second_ele = second_elements[0]
if first_ele == second_ele:
    print(first_elements+second_elements)
else:
    print('tuples cannot be joined')

elements = ((2,1),(3,8),(4,12),(2,9),(3,6))
for el in range(len(elements)):
    for ele in range(el+1,len(elements)):
        if elements[el][0] == elements[ele][0]:
            print(f'{elements[el]},{elements[ele]}')

# Python – Extract digits from Tuple list

items = [('hai','good',12,45.2,9,'fine')]
numbers = []
for item in items:
    if chr in item:
        if type(chr) == int or type(chr) == float:
           numbers.append(chr)
print(numbers)
    

# Python – All pair combinations of 2 tuples

first_elements = (2,5,1,3,6)
second_elements = (1,4,8,9,0)
pair = []
for num in first_elements:
    for nums in second_elements:
        pair.append((num,nums))
print(pair) 

# Python – Remove Tuples of Length K

elements = [(2,1,3),(3,8),(4,12,1,3),(2,9),(3,6)]
k = int(input('Enter the lenght to be removed:'))
removed = []
for i in elements:
    if len(i) == k:
        removed.append(i)
print(removed)


# Sort a list of tuples by second Item

# elements = [(2,1),(3,8),(4,12),(2,9),(3,6)]
# for i in range(len(elements)):
#     for j in range(len(elements)-1):