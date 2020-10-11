multi_line_string = """ I am A teacher"""
print(multi_line_string)
print(multi_line_string[0:2])
#reversing a String 
print(multi_line_string[::-1])

#convert the first letter of string to capital letters
challenge="thirty days of python"
print(challenge.upper())
#count() -> returns occurences of substring in string count(substring,start=..;, end=..)
print(challenge.count('y'))
#endswith() -> checks if a string ends with a specify ending.
print(challenge.endswith('thon'))

#formart
radius =21
PI=3.24
area = PI * radius ** 2

result ='The area of a circle of radius {}  is {}'.format(str(radius), str(area))
print(result)

#index() -> return the lowest index of a substring, sdditional urgument indicate starting and ending index(default 0)
sub_string ='ty'
print(challenge.index(sub_string))
#checks if character is alphanumeric
print(challenge.isalnum())
# check if all strings is alphabetc character
print(challenge.isalpha())
#is decimal
print(challenge.isdecimal())
#is digit 0-9
print(challenge.isdigit())
#is numeric
print(challenge.isnumeric())
#is lower case
print(challenge.islower())
#is upper case
print(challenge.isupper())

#join() -> return a concatenated string.
web_tech = ['HTML','CSS','JS','BOOTSTRAP']
res = '#'.join(web_tech)
print(res)

#strip() Remove all given characters starting from the beginning and end of string
print(challenge.strip('thon'))

#replace() -> replace substring with a given string
print(challenge.replace('python','JavaScript'))

#split()-> Split the string, using given string as a separator
print(challenge.split())

#title() -> Return a title case string
print(challenge.title())

#swapcase() ->covert all lowercase to uppercase and uppercase to lowercase 
print(challenge.swapcase())

#starts with:->Checks if the string starts with the specified string
print(challenge.startswith('Hey'))