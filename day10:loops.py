#While loop
# We use the reserved word while to make a while loop. It is used to 
# execute a block of statement repeatedely until a given condition is
# satisfied.When the condition becomes false then the line of code after the loop will be continued to execute.
    # count =0
    # while count < 5:
    #     print(count)
    #     count = count + 1
#While loop becomes false when the count is 5. That is when the loop stops.If we're 
# interested to run the code when the condition is no longer true, we can use else.

    # while count < 5:
    #     print(count)
    #     count = count +1
    # else:
    #     print(count)

#Break and continue
# We use the break when we like to get out of or stop the loop
# this loop only print 0,1,2 When it reaches 3 it stops. 

    # while count < 5:
    #     print(count)
    #     count = count +1
    #     if count ==3:
    #         break
#continue :We can stop current iteration and continue with the next
    # count =0
    # while count < 5:
    #     if count == 3: #only prints 0,1,2,4 (skips 3)
    #         continue
    #     print(count)
    #     count =count+1
    
#FOR LOOP
# used for iterations over sequesences. ie either a list,tuple,dictionary, set or string
# 1. FOR loop with LIST
numbers = [1,2,3,4,5,6]
for number in numbers:
    print(number)
    
#2. FOR LOOP with String

language = "Javascript"
for letter in language:
    print(letter)
    
#3. FOR LOOP in tuple
tuple_number = (0,1,2,3,4,5,6)
for num in tuple_number:
    print(num)

#FOR LOOP in DICTIONARY

person = {
    # key         values
    'first_name' : 'Collins',
    'last_name' : 'Jumah',
    'age' : 250,
    'country' : 'Kenya',
    'is_married' : False,
    'skills' : ['JavaScript','React','Node','Mongo','Python'],
    'address': {
        'street' :'Kawangware',
        'code' : 100100
    }
}

for key in person:
    print(key)

for key,value in person.items():
    print(key,value)
    
# Loops in SETS
it_companies = {'Zalego','Safaricom','AfricaStalking','DeCoded Africa','Apps:Labs'}
for company in it_companies:
    print(company)
    
#BREAK & CONTINUE part 2
# We use break when we want to stop our loop before its complete

positons = (1,2,3,4,5,6,7,8)
for num in positons:
    print(num)
    if num == 3:
        break
#the range Function
# used to loop through set of code certain number of times.
# the range(start,end, step) takes three parameters: starting,ending and the increment
# By default. it starts from 0 and increment by 1. the range the range sequence needs atleast one urgument(end)

lst = list(range(11))
print (lst)

st = set(range(1,11)) # 2 argument indicate the start and end of the sequence, step set to default 1
print(st)

lst = list(range(0,11,2))
print(lst)

for number in range (11):
    print(number)
    
# NEsted for...loop
for key in person:
    if key == 'first_name':
        for skill in person['skills']:
            print(skill)
            
#for...else
# if we want to execute some message when the loop ends

for numberr in range(12):
    print(numberr)
else:
    print('the loop ended at', numberr)
    
#PASS: When a statement is requeired after semi-colon, but we dont like to execute any code, 
# we can write the word pass to avoid any error,
#  also we can use it as a placeholder for future statement.

for num in range(5):
    print(num)
    pass

# Iterate 0 to 10 using for loop, do the same using while loop.

ite = 0

# while ite < 10:
#     print(ite)
#     ite= ite +1
# for l in range(11):
#     print(l)
    
while ite < 10 :
    if ite ==10:
        break
    print(ite)
    ite =ite -1
i='#'
while i in range(7):
    print(i)
    i=i+1