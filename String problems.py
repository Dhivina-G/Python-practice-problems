# 11. Python program to check if a string is palindrome or not

word = input('Enter a string:')
string_reverse = ''                            # initialize an empty string         
for letter in word:
    string_reverse = letter + string_reverse   # on each iteration the letters are concatenated to the empty string
if(word==string_reverse):                      # check if the gived word and reverse string are equal
    print('String is palindrome')
else:
    print('String is not palindrome')

def string_reverse(word):
    string_reversed = word[::-1]             # reverse slicing 
    return string_reversed
word = input('Enter a string:')
reversed_word = string_reverse(word)
if(reversed_word == word):
    print('String is palindrome')
else:
    print('String is not palindrome')


# 12. Python program to check whether the string is Symmetrical or Palindrome

# 13. Reverse words in a given String in Python 

string = input('Enter a string:')
string_reverse = string[::-1]              # using slicing
print(''.join(string_reverse))

string = input('Enter a string:')
string_reversed = ''                          # set an empty string
for char in string:
   string_reversed = char+ string_reversed    # on each iteration the letters are concatenated to the empty string
print(string_reversed)


# 14. Ways to remove i’th character from string in Python

string = input('Enter the string:')
character = input('Enter a character to remove:')
new_string = ''                                     # set an empty string
for letter in string:                               
    if( letter != character):                       # check if the character not presents
        new_string += letter                        # if not add rest of the character to new_string
print(new_string)


# 15. Python | Check if a Substring is Present in a Given String

string = input('Enter a string:')
substring = input('Enter a substring for string:')             
if substring in string:                               # check if the substrig present in string
    print('Substring is present')
else:
    print('Substring not present')

# 16. Python – Words Frequency in String Shorthands

string = input('enter the string:')
new_string = string.split(' ')           # split the word with space
count = {}                               # set a dictionary to count the words
for word in new_string:                    
    if word in count:                    # check if the word in count
        count[word] += 1                 # if present increase the count
    else:
        count[word] = 1                  # if not present assign as one
print(count)

# 17. Python – Convert Snake case to Pascal case

string = 'python_program'
new_string = string.split('_')        # split the underscore
new_word = ''                         # initialize a new empty string
for word in new_string:
    new_word += word.title()          # concantenate word and capitilze
print(new_word)


# 18. Find length of a string in python (4 ways)

string = input('Enter the string:')
length = len(string)
print('Length of the string =',length)

string = input('Enter the string:')
count = 0
for char in string:
    count += 1
print('Length of the string =',count)


# 19. Python program to print even length words in a string

string = input('Enter the string:')
new_string = string.split(' ')           # split the space
for word in new_string:                  # iterate through each word
    if(len(word)%2 == 0):                # check if the length of word is even
        print(word)

# 20. Python program to accept the strings which contains all vowels

string = input('Enter the string:')
vowels = ['a','e','i','o','u']            # intialize vowels
for letter in string:
    if(letter not in vowels):             # check if the letters in vowels
      print('String can be accepted')
      break
else:
    print('String cannot accept')


#  -----------------------------------------27/4/24-----------------------------------------------

# 1. Python | Count the Number of matching characters in a pair of string

string_1 = input('Enter the string:')
string_2 = input('Enter the second string:')
count = 0
for letter in string_1:
    for char in string_2:
        if(letter == char):
            count += 1
print(count)


# 2. Remove all duplicates from a given string in Python

string = input('Enter the string:')
new_string = ''
for letter in string:
    if(letter not in new_string):
        new_string += letter
print('After duplication:',new_string)


# 3. Python – Least Frequent Character in String

string = input('Enter the string:')
new = {}
for letter in string:
    if letter in new:
        new[letter] += 1 
    else:
        new[letter] = 1
print(new)
min_char = []
min_value = min(new.values())
for key,value in new.items():
    if value == min_value:
        min_char.append(key)
print(min_char)


# 4. Python | Maximum frequency character in String

string = input('Enter the string:')
new = {}
for letter in string:
    if letter in new:
        new[letter] += 1 
    else:
        new[letter] = 1
print(new)
max_char = []
max_value = max(new.values())
for key,value in new.items():
    if value == max_value:
        max_char.append(key)
print(max_char)

# 5. Python | Program to check if a string contains any special character

string = input('Enter the string:')
if string.isalnum():
    print('String does not contain special charater')
else:
    print('String contains special charater')

