# 1. Python program to interchange first and last elements in a list

list = [3,4,7,9,12,24]
first_number = list.pop(0)                      # assigning the first index element that is removed
last_number = list.pop(-1)                      # assigning the last index element that is removed
first_number_new = list.insert(0,last_number)   # inserting last_number to the zeroth position
last_number_new = list.append(first_number)     # appending first_number to first posiiton
print(list)

list = [3,4,7,9,12,24]
list[0], list[-1] = list[-1], list[0]    # swapping first and last element in the list
print(list) 

# 2. Python program to swap two elements in a list

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
