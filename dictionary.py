#starts and ends with {}
# used to store value in key-pair format
dictionary = {"key":"value"}
print(dictionary["key"])
#dictionary with multiple key-value pair
person = {
    'name': ('Collins','Jumah'),
    'age': 100,
    1:100
    }
print('name' in person)
print(person['name'])
person['city'] ="Nairobi"
print(person[1])
del person['age']
print(person)

#Challenge
#Make a dict with key value pair. Name,age and city

personalInfo = {
    'name' : "Collins Jumah",
    "age" : 39,
    "city" : "Busia"
}
print(personalInfo['name'])
print(personalInfo['city'])
#########Access a dictionary inside a list

languages =[ 
            {"name" : "Java","framework" : "SpringBoot"},
            {"name" : "PHP","framework" : "Laravel"},
            {"name" : "JavaScript", "framework" : "VueJS"} 
            ]
print(languages[2]['name'])

a = {"id": 5, "username": "collynes", "email" : "collins@gmail.com"}
b = {"id": 5, "username": "collynes", "email" : "jumah@gmail"}
print(a | b)

#unpacking syntax
print(**b, **a)