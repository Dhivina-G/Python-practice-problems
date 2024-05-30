# 21. Python – Extract Unique values dictionary values

# address_details = {'name':'Mark','place':'Delhi','age':29}
# for details in address_details.values():                    
#     print(details)


# 22. Python program to find the sum of all items in a dictionary

# numbers = {'one':2,'two':4,'three':29,'four':12}
# sum = 0                                    # set sum as zero
# for value in numbers.values():             # get the values in the dictionary]
#     sum += value                           # sum the values
# print(sum)


# 23. Python | Ways to remove a key from dictionary

# address_details = {'name':'Mark','place':'Delhi','age':29}
# del address_details['name']                                # delete using del
# print(address_details)


# 24. Ways to sort list of dictionaries by values in Python – Using itemgetter

# from operator import itemgetter                                             # imported itemgetter 

# address_details = [{'name':'Mark','place':'Delhi','age':29},{'name':'Serin','place':'Mumbai','age':31},{'name':'John','place':'Kerala','age':41}]
# sorted_address = sorted(address_details,key=itemgetter('age'))               # sorted the dictionary using itemgettr as key 
# print(sorted_address)

# 25. Ways to sort list of dictionaries by values in Python – Using lambda function

# address_details = [{'name':'Mark','place':'Delhi','age':29},{'name':'Serin','place':'Mumbai','age':31},{'name':'John','place':'Kerala','age':41}]
# sorted_address = sorted(address_details,key=lambda value:value['name'])
# print(sorted_address)


# ---------------27/8/24-------------------------------------

# Python – Append Dictionary Keys and Values ( In order ) in dictionary

# dictionary = {}
# n = int(input('Enter the range:'))
# for i in range(n):
#     key = input('Enter the key:')
#     value = input('Enter the value:')
#     dictionary.update({key:value})
# print(dictionary)


# Python | Sort Python Dictionaries by Key or Value

# details = {'name':'Serin','place':'Mumbai','age':31}
# new_details = sorted(details.items())
# print(new_details)

details = {'name':'Serin','place':'Mumbai','address':'xyz'}
details_list = []
for val in details.values():
    details_list.append(val)
print(details_list)
details_sort = sorted(details_list)
new_details = {}
for i in details_sort:
    for j in details.keys():
        if details[i] == details[j]:
            new_details[j]=i
print(new_details)
    


# Python – Sort Dictionary key and values List

# details = {'name':'Serin','place':'Mumbai','address':'xyz'}
# details_key = []
# details_val = []
# for key in details:
#     details_key.append(key)
# print(sorted(details_key))
# for val in details.values():
#     details_val.append(val)
# print(sorted(details_val))

# Handling missing keys in Python dictionaries

# number = {'one':1,'two':2,'three':3,'four':4}
# element = input('enter a key value:')
# try:
#     if element not in number:
#         raise Exception 
#     else:
#         print('key found')
# except Exception as e:
#     print('key not found')


# Python dictionary with keys having multiple inputs



