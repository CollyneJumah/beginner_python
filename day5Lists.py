#LIST::: Is  a collection which is ordered and changeable(modified). 
        # Allow duplicate member.
#TUPLE:::Is a collection which is unordered and unchangeable or unmodified(unmutable).
        # Allows duplicate member.
#SET:::Is a collection which is unordered, unindexed and unmodified but you can add new item.
        # No duplicate member.
#DICTIONARY::: Is a collection which is unordered, changeable(modifiable) and indexed. 
        # No duplicate member.
        
# A list is a collection of different data types which is ordered and modifiable(mutable). 
# It can be empty or may have different datatype items

#HOW TO CREATE A LIST
#1. Using List built-in function
from os import truncate


lst= list()
empty_list = list()
print(len(empty_list))

#2. using square brackets [].
lst = []

#####################################
fruits= ['Mangoes','Oranges','Bananas','Pineapple']
veges =['cabbage','sukuma wiki','Kunde','Murenda']
animal_products = ['meat','butter','milk','skin','yoghurt']
web_techs = ['HTML','CSS','REACT','REDUX','VUE']
countries = ['Kenya','Serbia','Uganda','Tanzania','Ethiopia']

print('Fruits:', fruits, 'Number Of Fruits:', len(fruits))
print('Vegetable:' ,veges)
print(veges[2])
print(web_techs[-3])#accessing from the end begin -1,-2,-3

#unpacking list items
lis = ['item1','item2','item3','item4','item5']
first,second,third,*rest = lis
print(rest)

#slicing items in the list.
#1. Positive indexing
all_fruits= fruits[1:4]
print(all_fruits)

#reversing list 
# the reverse()
fruits.reverse()
# sorting list items
# sort() re-orders the list items in ascending order and modifies the original list. 
# If the urgument of sort() method reverse is equal to true, it will arrange the list in descending order
fruits.sort()
fruits.sort(reverse=True)