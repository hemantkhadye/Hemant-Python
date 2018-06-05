

#######################################################################
# Getting to know the basics : If, elif & else
#######################################################################

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("You've reached the kitchen area.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print("Needs more space.")


# Define variables
room = "hall"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "hall":
    print("looking around in the hallway.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size place.")
else :
    print("needs more space.")



#######################################################################
# Excercise
#######################################################################

# Write a code to check if a number is even or not. Use if statement and use % operator.
z = 5
if z % 2 == 0:
    print('number '+ str(z)+ ' is even')

# Write a code to check if a number is divisible by 2 or 3. Use % operator and elif statement.
z = 5

if z % 2 == 0:
    print('number ' + str(z) + ' is divisible by 2')
elif z % 3 == 0:
    print('number ' + str(z) + ' is divisible by 3')
else:
    print('Number neither divisible by 2 or 3')


# Print 'yes, present' as output if number is present in the list l, else print 'no'

l = [4,5,6,7,8]
number = 3
if l.__contains__(number):
    print('yes, present')
else:
    print('no')



