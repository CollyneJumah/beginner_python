gueze=10
answer=10


if gueze == answer:
    message ="You win"
elif gueze < answer:
    message = "Your gueze is too low"
elif gueze > answer:
    message = "Your gueze is too high"
print(message)
## challenge


if num == 4:
    print("Its 4")
elif num > 4:
    print("Your num "+str(num)+ " is higher than expected")   
else:
    print("Too small")
    

for num1 in range(1,101):
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    else:
        print(num)