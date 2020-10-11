tvShow = ['Maria','JKLive','Tsunami','Papa Shirandula']
print(tvShow)
print(tvShow[3])
#add more items on the list
tvShow.append('Nipashe Wikendi')
print(tvShow)
#remove items on the list
tvShow.remove(tvShow[1])
print(tvShow)

#insert on aa given position
tvShow.insert(3,"Time")
print(tvShow)
#############################end ###############################
square =[1,4,9,16,25,36,49]
print(square[-5:]) #slicing return new list
#all slicing operation returns a new list containing the requested elements. 
# this means the following slice returns a shallow slice of copy
print(square[:])
concate = square + [64,81,100,121]
print(concate)
############## challenge##########
# Make an empty list and asign to a variable fav_food
#Add two items
#print the second item
#remove the first item

fav_food =[]
fav_food.append("fish")
fav_food.append('beans')
print(fav_food[1])
fav_food.remove(fav_food[0])
print(fav_food)
#removing item using pop
lst =['item1','item2','item3']
lst.pop(1)
print(lst)

#removing using del
#the del keyword remove the special index and it can also be used to delete items within index range.
#It can also delete index completely,
fruits = ['bananas','orange','mango','lemon','kiwi','lime']
del fruits[0]
print(fruits)
del(fruits[1:3]) #delete items between index, so this does not delete item with index 3
print(fruits)
#clear List using clear()
fruits.clear()
print(fruits)

#copyinng list
fruits_copy = fruits.copy()

print(fruits_copy)
#joining list
# using + operator
positive_numbers =[1,2,3,4,5,6,7]

negative_number = [-1,-2,-7,-9]

join=positive_numbers + negative_number
print(join)
#joining using extend()

list1=['item1','item2','item3']
list2 = ['item4','item5']
list1.extend(list2)
print(list1)
#countng items in a list ->returns the number of times an item appears in a list.
countList = list1.count('item3')
print(countList)
#finding index of an item
# the index() method returns the index of an item in a list
