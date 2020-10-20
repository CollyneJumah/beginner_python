def hello():
    print('Collins Jumah')
    
hello()

def multiply(num1,num2):
    print(num1 * num2)
    
multiply(3,5)

#Functions without paramemters
def general_info ():
    first_name = 'Collins'
    last_name ='Jumah'
    full_name = first_name + ' '+ last_name
    print(full_name)
general_info()

def add_two_numbers () :
    num1 =30
    num2 =50
    sum=num1 + num2
    print(sum)
add_two_numbers()

#function returning a value
def personal_info():
    fname="My name is"
    lname="collins jumah"
    full = fname + " " + lname
    
    return full
print(personal_info())

#functions with parameters
# in a functions we can pass different data-types
# (number,string,boolean,list,tuple,dictionary or set) as parameters
# IF a function takes a parameter, we should call it with an argument

def greetings(name):
    message = name + ', Welcome to Python Is Easy.'
    return message
print(greetings('Collins Jumah'))

def addTen(num):
    ten =20
    return num + ten
print(addTen(300))

def squareNumber(x):
    return x * x
print(squareNumber(20))

def square_of_circle(r):
    PI = 3.142
    area = PI * r**2
    return area
print(square_of_circle(7))

def sum_of_num(n):
    total =0
    for i in range(n+1):
        total +=i
    print(total)
    
sum_of_num(10)
    
#two parameters
def general_full_name(firstName,lastName):
    fullName = firstName + " " + lastName
    return fullName
print(general_full_name("Donny Van", "De Beek"))

def sum_of_two_numbers(num1,num2):
    sum = num1 + num2
    return sum
print(sum_of_two_numbers(120,90))

def calculate_age(current_year,birth_year):
    age = current_year - birth_year
    return age
print(calculate_age(2020,1995))

def weight_of_object(mass,gravity):
    weight = str(mass * gravity) + 'N'
    return weight
print(weight_of_object(100,9.89))

# Passing argument with key and value: Here the order of the
# argument does not matter...

def personal(firstName,fullName):
    name= firstName + " " + fullName
    print(name)
personal(
    firstName="Collins",
    fullName="Jumah"
)

# function returning a value
# If we do not return a value by our function, then its returning NONE by 
# default.To return a value by a function we use a keywordreturn followed by the 
# variable we are returning.We can return any kind of data type from a function
# 1.Returning a string
def print_name(name):
    return name
print_name('Collins')

# returning a boolean
def is_even(n):
    if n % 2 ==0:
        print('even')
        return True
    return False
print(is_even(10))

#returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(21))

#function with default parameter
def greet(name="Collins"):
    message = name+" Welcome home"
    return message
print(greet())
print(greet('Jumah'))

def myname(fname="Miriam", lname="Juma"):
    name=fname +" "+lname
    return name
print(myname())
print(myname('Mourine', 'Juma'))

#calculate age
def myAge(birth_year,current_year=2020):
    age= current_year-birth_year
    return 'I am ' + str(age)+" years old."
print(myAge(1995))

def weight_of_object(mass,gravity=9.81):
    weight= str(mass * gravity)
    return weight
print("Weign Is: " + weight_of_object(200)+ "N")

#Abitrary Number
#If we do not know the number we're passing to a function, 
# we can create a function which can create arbitrary number of urguments by adding * before the parameter name.

def sum_all_num(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(sum_all_num(2,3,4,5))

#Default arbitrary number
def generate_group(team, *args):
    print(team)
    for i in args:
        print(i)
generate_group('Team1','team3')

#function as parameter of another function
def square_number(n):
    return n*n
def do_something(f,x):
    return f(x)
print(do_something(square_number,3))
