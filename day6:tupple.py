#collection of different data type which is ordered and unchangeable(Immutable)
# written in round brackets ()
# Once created its value cannot be changed,
# We cannot use add, insert, remove methods coz its not modified
# Methods related to tuple are: 
# tuple() > to create an empty tuple
#count() > to count the number of a specified item in tuple
# index: to find the index of a specified item in a tuple
#operator . : to join more tuple and to create a new tuple

# 1.Creating empty tuple
empty_tuple = ()
empty_tuple = tuple()  #using the tuple constructor

#tuple with initial value
tpl = ('item1','item2','item3','item4')

#tuple length
#we use len() to get the legth of a tuple
print(len(tpl)) 

#accessing tuple item
first_item = tpl[2]
print(first_item)

#Negative indexing:: Hear it means beginning from the end , -1 refers to the last item, -2 refers to the seond last, 
last_item=tpl[-3]
print(last_item)

#slicing tuple
# We can slice out subtuple by specifying a range of indexes where to start and where to end in the tuple.The return value will be a new tuple with specified items
#1.range of positive indexes
allitems = tpl[0:4]
allitems = tpl[0:]
middleTwo = tpl[1:3] #doent include item in index 3
item2_to_the_rest = tpl[1:]

#range of negative index
last_item_to_the_rest = tpl[-4:]

#changing tuple to list
# We can change tuple to list and list to tuple.
#tuple is immutable If we want to modify a tuple we should change it to a list.
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print(lst)
lst[0] ='item0'
print(lst)
lst = tuple(lst)
print(lst)

#checking an item in a list
#we can check if an item exist in a list using in, returns a boolean
print('item3' in tpl)

#join tuple
#we can join two or more tuple using + operator
tpl1 = ('Mango','Bana')
tpl2 = ('cabbage', 'sukuma')
print(tpl1 + tpl2)

#deleting tuple::: Its not possible to remove a single item in a 
# tuple but it's possible to delete the tuple itself using del
del tpl1
