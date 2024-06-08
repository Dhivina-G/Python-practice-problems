#  1. Python program to interchange first and last elements in a list

list = [3,4,7,9,12,24]
first_number = list.pop(0)                       # assigning the first index element that is removed
last_number = list.pop(-1)                       # assigning the last index element that is removed
first_number_new = list.insert(0, last_number)   # inserting last_number to the zeroth position
last_number_new = list.append(first_number)      # appending first_number to first posiiton
print(list)

list = [3,4,7,9,12,24]
list[0], list[-1] = list[-1], list[0]    # swapping first and last element in the list
print(list) 

#  2. Python program to swap two elements in a list

list = [3,4,8,12,33,62]
first_number = int(input('Enter the value from list:'))                                      # get the number that need to br swaped
first_num_index = list.index(first_number)                                                   # index of first numbr
second_number = int(input('Enter the value from list:'))                                     # get the number that need to br swaped
second_num_index = list.index(second_number)                                                 # index of second number
list[first_num_index],list[second_num_index] = list[second_num_index],list[first_num_index]  # swaped using index positions
print(list)


# 3. Python | Ways to find length of list

def length_of_list(list):
    length = len(list)         # len() finds the length of list
    return length
list = [3,7,2,14,28,72]
print(length_of_list(list))

lists = [3,7,2,14,28,72,99]
count = 0                           # set count to zero
for list in lists:                  # to iterate over the list
    count += 1                      # increase the count by 1 in each iteration
print('Length of list =', count)
 

# 4. Python | Ways to check if element exists in list

list = [1,4,3,12,9,36,77]
element = int(input('Enter the number :'))
if element in list:                              # in operator is used to check whether the element exists in a sequence 
    print(element,'is present in the list')
else:
    print(element,'is not present in the list')

lists = [1,4,3,12,9,36,77]
element = int(input('Enter the number:'))
for list in lists:                            
    if list == element:                           # checked if the list value equals to the element 
        print(f'{list} present in the list')
        break
else:
    print(f'{element} is not present')


# 5. Different ways to clear a list in Python

list = [1,2,3,4,8]
list.clear()                          # clear() removes all items from list
print(list)

list = [1,2,3,4,8]
list = []                             # list is assigned as empty
print(list)

list = [1,2,3,4,8]
del list[:]                           #  del used to delete items
print(list)

list = [1,2,3,4,8]
for num in range(len(list)-1,-1,-1):    # iterate in reverse order
    list.pop(num)                        # pop items from last
print(list)


# 6. Python | Reversing a List

list = [1,2,5,11,29,44]
list.reverse()                     # reverse the items in the list
print(list)

list = [1,2,5,11,29,44]
list_new=list[::-1]                # negative slicing
print(list_new)

list = [1,2,5,11,29,44]
reverse=[]                        # set reverse as empty list
for num in list: 
    reverse.insert(0,num)           # inserting elements to the first position
print(reverse)


# 7. Python program to find sum of elements in list

def sum_of_list(list):
    sum = 0                  # initialize sum as zero
    for lst in list:
        sum += lst           # adding each value in list to sum 
    return sum
list = [4,9,2,13,28,1]
print(sum_of_list(list))


# 8. Python | Multiply all numbers in the list

def product_of_list(list):
    product = 1                   # initialize product as one
    for lst in list:
        product *= lst            # multiply each value in list to product
    print(product)
product_of_list([1,2,3,4,5,6])


# 9. Python program to find smallest number in a list

list = [22,18,51,73]
smallest_value = list[0]                         # set smallest value as first element in the list
for lst in range(len(list)):
    if list[lst] < smallest_value:              # compare each value with the smallest value
        smallest_value = list[lst]               # if the compared value is less than smallest_value ,set the value as smallest
print('Smallest number is :',smallest_value)


# 10. Python program to find largest number in a list

list = [1,2,13,28,56,31]
largest_value = list[0]
for lst in list:
    if lst > largest_value:                        # compare each value with the largest_value
        largest_value = lst                        # if the compared value is greater than largest_value ,set the value as largest
print(f'Largest number in list:{largest_value}')


# ----------------------------27/05/24---------------

#  1. Python program to find second largest number in a list

list = [2,4,1,5,13,73]
new_list = sorted(list)
print(new_list)
second_largest = new_list[-2]
print(second_largest)



# 2. Python program to find N largest elements from a list

list = [3,1,44,52,12]
n = int(input('Enter the limit:'))
new_list = sorted(list)
largest_elements = new_list[-n:]
print(largest_elements)


# 3. Python program to print even numbers in a list

list = [2,4,6,1,3,7]
for num in list:
    if num %2 == 0:
        print(num)

#  4.  Python program to print odd numbers in a List
list = [2,3,12,11,17,22]
for num in list:
    if num %2 != 0:
        print(num)

#  5. Python program to print all even numbers in a range

start_limit = int(input('Enter the start range:'))
End_limit = int(input('Enter the end range:'))
for num in range(start_limit,End_limit):
    if num % 2 == 0:
        print(num)
    num+=1


# -----------------------31/05/24----------------------------

# 1. Python program to print all odd numbers in a range

start_limit = int(input('Enter the limit:'))
End_limit = int(input('Enter the end limit:'))
for num in range(start_limit,End_limit+1):
    if num %2 != 0:
        print(num)


# 2. Python program to print positive numbers in a list

list = [2,-1,5,-7,18]
for num in list:
    if num > 0:
        print(num)


# 3. Python program to print negative numbers in a list

list = [2,-3,6,-7]
for num in list:
    if num < 0:
        print(num)


# 4. Python program to print all positive numbers in a range

start_limit = int(input('Enter the start limit:'))
End_limit = int(input('Enter the end limit:'))
for num in range(start_limit,End_limit+1):
    if num > 0:
        print(num)


# 5. Python program to print all negative numbers in a range

start_limit = int(input('Enter the start limit:'))
End_limit = int(input('Enter the end limit:'))
for num in range(start_limit, End_limit+1):
    if num < 0:
        print(num)


# 6. Remove multiple elements from a list in Python

values = [3,2,11,65,38,5]
element_one = int(input('enter the element to be removed:'))
element_two = int(input('Enter the element to be removed:'))
new_list = [element_one,element_two]
for val in values:
    if val in new_list:
        values.remove(val)
print(values)

# 7. Python – Remove empty List from List

elements = [[2,3,4,12,28],[],[9,12,34,55],[4,63,0,1,5]]
new_element = []
for num in elements:
    if num != []:
        new_element.append(num)
print(new_element)

# 8. Python | Cloning or Copying a list

def cloning(lst):
    new_list = lst
    return new_list
words = ['good','come','find','look']
print(cloning(words))

# 9. Python | Count occurrences of an element in a list

numbers = [2,4,1,92,4,14,9,0]
new_list = {}
for num in numbers:
    if num in new_list:
        new_list[num] += 1
    else:
        new_list[num] = 1
print(new_list)

numbers = [2,4,1,92,4,14,9,4]
element = int(input('Enter the element:'))
count = 0
for val in numbers:
    if val == element:
        count += 1
print(f'count of {element} is {count}')

numbers = [3,4,1,92,4,64,3,4]
element = int(input('Enter the element:'))
for val in numbers:
    times = numbers.count(element)
print(f'Number of times {element} occure = {times}')

# 10. Python | Remove empty tuples from a list

elements = [(2,3,4,12,28),(),(9,12,34,55),(4,63,0,1,5)]
new_element = []
for num in elements:
    if num != ():
        new_element.append(num)
print(new_element)
