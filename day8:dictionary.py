#A collection of unordered, modifiable(mutable) pair(key:value) data type
#We use curley brackets to create {}
dct = { 'key1':'value1', 'key2':'value2','key3':'value3'}
person = {
    "Name" : "Collins Jumah",
    "Location" : "Nairobi",
    "age" :25,
    "country" : "Kenya",
    "is_married": False,
    "skills" : ['JavaScript','Python','PHP'], #tuple
    "address" : { #set
        "street" : "Kawangware",
        "zipcode":"02000"
    }
}

#Dictionary Length: It checks the number of key:pairs in the dictionary
print(len(person))

#Accessing dictionary items
#We can access by referring to its key name
print(person['Location'])

#Accessing an item gives an error first check if the key exist by using get() which returns none(A None Type object data type)

print(person.get('age'))

#Adding item to dictionary
person['phone'] = '0790366848'
# person['email'].append('collins@gmail.com') # not woring
print(person)

#Checkign key in the dictionary
print('key2')

#remove key and valuepair
# pop(keyname)
# popitem() remove the last item
#del remove a item with specified key name
person.pop('Name')
person.popitem()
del person['Location']
print(person)

#changing dictionalry to a list. We use item()
print(person.items())
print(person)

#clearing a dictionary using clear()
print(person.clear())

#copy a dictionary using copy(). 
dic_copy = person.copy()
print(dic_copy)

#getting dictionary key as a List . The key() gives all dictionary keys as a list
keys = person.keys()

#getting dictionary values as a list we use the values()
values= person.values() 

#deleting a Dictionary
del person



 