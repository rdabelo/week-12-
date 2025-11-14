# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collections family in 
# Examples:
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) #5
print(type(my_list)) # <class 'list'>
print(my_list[0]) #1
print(my_list [1:4]) # [2,3,4]
print(my_list[1:]) # [2,3,4,5]
print(my_list [:-1]) # [1,2,3,4]
#reverse list
# print(my_list [::-1]) #[5,4,3,2,1]
# my_list = ['apple', 'banana', 'cherry']
#modifying a list
my_list.append(6) # adds 6 to the end of the list
print(my_list) # [1, 2, 3, 4, 5]
# add 7 and 6 to the end of the list
my_list.extend ([7, 8])
print(my_list) # [1,2,3,4,5,6,7,8,]
#remove the last item
my_list.pop()
print(my_list) # [1,2,3,4,5,6,7]
#remove the item at index 2
my_list.pop(2)
print(my_list) # [1,2,4,5,6,7,]
#sort the list in ascending order
my_list.sort()
print(my_list)
#reverse the list
my_list.remove(4)
print(my_list)
#remove specific value
my_list.remove(4)
print(my_list)
#remove the last item using negative index
my_list.remove(-1)
print(my_list)
#add 50 more or more to the end of the list
new_list= list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
new_list(range(12, 320))
print(my_list)
every_thirdnumber = my_list[::3]
print(every_thirdnumber[::3])
del my_list[ : : 3]
print(len(my_list))
print(my_list)

#list functions
# .appennd() - adds an item to the end of the list
# . extend() - adds muiltpiple items to the end of the list
# .pop() - removes and returns an item at a given index
# (default is the last item)
# .remove() - removes the first occurence of a specefic value
#.sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list
# why is a list more useful than a variable?
# a list can hold multiple values,
#while a variable can only holy one value at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
# acces the first time
print(cakes[0])# chocolate
# access the last item
print(cakes[-1]) # carrot
# want to chocalate cake indeat of vanilla
cakes [0] = 'strawberry'
print(cakes)  # ['strawberry, vanilla, red velvet", carrot]
# add a nmew cake to the end of the list
cakes.append('lemon')
print(cakes)
caks[1]= chocalate
print(cakes)
#remove the last cake
cakes.pop()
print(cakes)
# insert a new cake at the index 2
cakes.insert(2, 'funfetti')
print(cakes)



print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.