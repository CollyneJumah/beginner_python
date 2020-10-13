#collection of unordered or unindexed distinct elements. 
#Used to store unique items and its possible to fid the union, intersection, difference, symmetric difference, subset,superset and disjoint
#We use curly brackets

st ={}
#or
st = set()

#initial items
st ={'Banaba', 'oranges','pineapple','mangoes'}

#getting set length:> We use len()

len(st)

#accessing items in a set. We use loop
#to check if an item exist we use in

'mangoe' in st

#Once set is created we cannot change but we can add items using add()

st.add("pizza")

#Add multiple items using update()
st.update(['youghyt','mikl'])

#remove items by using remove(), if item does not found, it will displya an error. Otherwise you can use discard()
#clearing items
st.clear()

#deleting a set
del st
#converting list to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)

#joining sets
set1 ={'Java','PHP','Dart','Go'}
set2 ={'Sprint Boot','Laravel','GoLang'}

set3 = set1.union(set2)
print(set3)

#inserting a set into a given set
set1.update(set2)
print(set1)

#Intersecting a set. this returns items which are in both sets 
webProgramming = {'Python','JavaScript','Java','PHP','Go','Ruby'}
applicantions = {'JavaScript','Java','C#','.Net'}
print(webProgramming.intersection(applicantions))

#Checking a subset and a superset
#A set can be a subset or superset of other set
#Sub set:: issubset()
#Super set :: issuperset()
example1 = {'item1','item2','item3','item4','item5'}
example2 = {'item3','item5'}

print(example2.issubset(example1))
print(example1.issuperset(example2))

#checking the difference between two sets. this returns the difference between two sets
print(example2.difference(example1))
print(example1.difference(example2))

#finding Symmetric difference of two sets
# It returns symmetric difference btween two sets. it means that it returns the set containing all 
# items from both sets, exept items that are present in both set
# (A\B) U (B\A)
#
print(example1.symmetric_difference(example2))

python ={'p','y','t','h','o','n'}
dragon = {'d','r','a','g','o','n'}
print(python.symmetric_difference(dragon))

# Joining sets
#If two sets do not have a common items / item we call them disjoint sets. 
# We can check if set is join or disjoint by using isdisjoint()
print(python.isdisjoint(dragon))
