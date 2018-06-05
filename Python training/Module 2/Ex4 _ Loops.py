
#######################################################################
# Getting to know the basics : Loops
#######################################################################

# While loop

# Initial error
error = 50

while error > 1:
    error = error/4
    print(error)
print('')


# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print('correcting...')
    offset = offset - 1
    print(offset)
print('')


# Add conditional statements
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    if offset > 0:
        offset -= 1
    else:
        offset += 1
    print("correcting...")
    print(offset)
print('')


# For loop
heights = [1.71, 2.2, 1.48, 2.0, 1.56]

for height in heights:
    print(str(heights.index(height))+ ' ' + str(height))
print('')

for c in 'heights':
    print(c.capitalize())
print('')

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for h in house:
    print('the ' + h[0] + ' is ' + str(h[1]) + ' sqm')
print('')

# looping over a dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'bonn',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'australia': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print('the capital of ' + key + ' is ' + value)


#######################################################################
# Excercise
#######################################################################

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use enumerate to print index and value of areas list.
for i, v in enumerate(areas):
    print(i, v)






