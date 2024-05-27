# 21. Python – Extract Unique values dictionary values

address_details = {'name':'Mark','place':'Delhi','age':29}
for details in address_details.values():                    
    print(details)


# 22. Python program to find the sum of all items in a dictionary

numbers = {'one':2,'two':4,'three':29,'four':12}
sum = 0
for value in numbers.values():   
    sum += value               
print(sum)


# 23. Python | Ways to remove a key from dictionary

address_details = {'name':'Mark','place':'Delhi','age':29}
del address_details['name']
print(address_details)


# 24. Ways to sort list of dictionaries by values in Python – Using itemgetter

# 25. Ways to sort list of dictionaries by values in Python – Using lambda function

address_details = [{'name':'Mark','place':'Delhi','age':29},{'name':'Serin','place':'Mumbai','age':31},{'name':'John','place':'Kerala','age':41}]
sorted_address = sorted(address_details,key=lambda value:value['name'])
print(sorted_address)

