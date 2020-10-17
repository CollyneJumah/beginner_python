#if condition
# if condition:
    # this part of code runs for truthy condition
a=24

if a > 0:
    print ('A is a positive number')
    
#ElSE
# if condition:
#      this part of code runs for truthy condition
# else:
    # this part runs for falsey condition
age = 13
if age > 18 :
    print( "You are allowed to vote")
else:
    print("You are not allowed to vote")

#If...Elif...Else
# In our daily life, we make decisions on daily basis.
#  We make decisions not by checking one or two conditions but multiple conditions. As similar to life,
#  programming is also full of conditions. We use elif when we have multiple conditions.
if a > 0:
    print("A is greater than Zero, A positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is Zero")

#shorthand
print("A is positve") if a > 0 else print('A is Negative')

#Nested conditions
if a > 0:
    if a % 2 == 0:
        print("A is a positive-Even number")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")
    
#if condition and logic
if a > 0 and a % 2 == 0:
    print('A is a positive even number')
elif a > 0 and a % 2 != 0:
    print('A is positve')
elif a < 0:
    print('A is negative')
else:
    print('A is zero')
    
#Exercise
enter_age = input("Enter Age:")
remainder = 18 - enter_age
if enter_age > 18:
     print("You are old enough to drive.")
else:
    print(f"You need %d more years to drive." %(remainder) )