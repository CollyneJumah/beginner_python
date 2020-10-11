name = "collins Jumah"
age =24
career ="Software Development"
place ="Nairobi"
print(name)

concate = "My Name is "+str(name) + ". I am "+str(age)+" years old. Iam a "+str(career)
print(concate)
#using placeholder
#format()->formart strings into a nicer output
placeholder ="My name is {}. I am {} years old, and I work as a {} .".format(name,age,career)
print(placeholder)
#specifying which variable is used where
placeholder2= "My name is {2}, I am {0} years Old. I leave at {3} and I am a {1} .".format(age,career,name,place)
print(placeholder2)

#fstring
fstring = f"Hello My name is {name}. I am {age} years old and I leave at {place}"
print(fstring)

myName = input("Please Enter your name:")
print(myName)
fprint=f"Hello {myName}"
print(fprint.upper())
