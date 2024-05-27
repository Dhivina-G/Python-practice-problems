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
if substring in string:
    print('Substring is present')
else:
    print('Substring not present')

# 16. Python – Words Frequency in String Shorthands
# 17. Python – Convert Snake case to Pascal case

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

# string = input('Enter the string:')
# for word in string:
#     if(len(word)%2 == 0):
#         print(word)

# 20. Python program to accept the strings which contains all vowels

