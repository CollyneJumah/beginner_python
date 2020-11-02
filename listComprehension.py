# A compact way of creating a list from a a sequence
# It's a short way to create a new list. It's considered faster than processign list using a for loop

# syntax
# [i for i in iterable if expression]
language = "Python"
lst =list(language)  #changing the string to list
print(type(lst))
print(lst)

# using list comprehension
listC = [i for i in language]
print(type(listC))
print(listC)

# If you want to generate list of number
number = [i for i in range(11)] # generate number from 0-10
print(number)

# performing mathematical operation during iteration
squares =[i * i for i in range(11)]
print(squares)

# making a list of tuple
numbers= [(i, i*i) for i in range(11)]
print(number)

# List Comprehension can be combined with if expression
# generating even number
even_number = [i for i in range(21) if i % 2 ==0]
print(even_number)

# generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 !=0 ]
print(odd_numbers)

# filtering numbers, i.e filtering positive even numbers
numbr =[-8,-7,-3,-1,0,1,3,4,5,7,6,8,10]
positive_even_number = [i for i in numbr if i % 2 == 0 and i>0]
print(positive_even_number)

# Flattering a 3D array
three_dimension_list =[ [1,2,3],[4,5,6],[7,8,9] ]
flattenedList = [ number for row in three_dimension_list for number in row]
print(flattenedList)

# Lamda function
# A small anonynmous function without a name. It can take any number of arguments. but can only have one expression. 
# Similar to anonymous functions in JS. We need it when we want to write an anonymous function inside another function.
# We use labda keyword followed by a parameter(s), followed by an expression(s)

# syntax: x= lambda param1,param2,param3: param1+param2+param3
            # print(x(arg1,arg2,arg3))
def add_two_function(a,b):
    print(add_two_function(4,5))
    
# self invoking lambda
(lambda a,b:a+b)(2,3) 

square = lambda x: x**2
print(square(3))

cube = lambda y: y**3
print(cube(3))

# multiple variables

multiple_variable = lambda a,b,c: a ** 2 - 3 *b +4 * c
print(multiple_variable(5,5,3))

# Lambda function inside another function
def power(x):
    return lambda n: x** n
cube = power(2)(5)
print(cube)
two_power_of_five =power(2)(5)
print(two_power_of_five)

# filter only -ves and zero in the lst using list comprehension
nums = [-4,-3,-2,-1,0,2,3,4,6]
negatives_and_zeros = [i for i in nums if i <= 0]
print(negatives_and_zeros)

