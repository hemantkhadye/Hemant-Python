
#######################################################################
# Getting to know the basics : Functions & Methods
#######################################################################

# Create variables var1 and var2
var1, var2 = [1, 2, 3, 4], True

# Print out type of var1
print(type(var1))

# Print out length of var1
print('length of var1: ' + str(len(var1)))

# Convert var2 to an integer: out2
out2 = int(var2)
print(str(out2) + ' ' +str(type(out2)))
print('')

# Most commonly used functions on lists
# len function : calculates the length
print('length of poolhouse: ' + str(len('poolhouse')))
print('length of var1: ' + str(len(var1)))

# max function : Calculates the maximum values in a list
print('Max value in var1: ' + str(max(var1)))
print('')

# Enumerate
l = ['Hello', 'Hi', 'Greetings', 'Okay']
e = enumerate(l)
e1 = list(e)
for i in e1:
    print(i)
print('')

# Sum of a list
print('Sum of first 4 numbers: ' + str(sum([1,2,3,4])))
print('')

# Methods
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()
print('Upper example: ' + room_up)

# Print out room and room_up
print('Capitalize example: '+ room.capitalize())

# Print out the number of o's in room
print('Count example: '+ str(room.count('o')))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Index function : Print out the index of the element 20.0
print('Index example: ' + str(areas.index(20.0)))

# Count method : Print out how often 14.5 appears in areas
print('Count example: '+ str(areas.count(14.5)))

# Append method : Append number 50 to the areas list and print it
areas.append(50)
areas.append([60,70])
print('Append example: '+ str(areas))

# Pop method : Removes and prints the the removed element
print('Pop example: ' + str(areas.pop(-1)))

# Extend method : Extend the list by adding 60,70
areas.extend([60,70])
print('Extend example: ' + str(areas))

# insert method : inserts an element in a list
areas.insert(0, 1)
print('insert example: ' + str(areas))

# Remove method : Remove 9.50 from the list
areas.remove(9.5)
print('Remove example: ' + str(areas))

# Reverse method : Reverses the list
areas.reverse()
print('Reverse list example:' + str(areas))

# Sort method : Sorts a list
areas.sort()
print('Sort list example: ' + str(areas))
print('')


#######################################################################
# Excercise
#######################################################################

# Append number 30 to areas list and reverse the list and print the output
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas.append(30)
areas.reverse()
print(areas)


# Use enumerate on the reversed list and print the output.
ea = enumerate(areas)
rel = list(ea)
print(rel)

help(list.sort)
# Sort the following list by length of the elements, shortest element should appear first.
l = ['Hello', 'Hi', 'Greetings', 'Okay']
l.sort(key=len)
print(l)



# Use insert method : insert 2 elements 'test1' and 'test2' in the list l at index 2.
l.insert(2, 'test1')
l.insert(2,'test2')
print(l)

# Quick check : What should be the output of this line of code?
l.clear()
print(l)

