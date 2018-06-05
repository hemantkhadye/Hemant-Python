
#######################################################################
# Getting to know the basics : Lists
#######################################################################

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print('Initial list: ' + str(areas))

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room",liv, "bedroom", bed, "bathroom", bath]

# Print areas
print('Refined list: ' + str(areas))

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Print 3 elements from areas
print(areas[1:4])


# List subsetting : house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
#print(areas[-3:-1])

#######################################################################
# Excercise
#######################################################################

# Sum of kitchen and bedroom area from areas list: eat_sleep_area
eat_sleep_area = areas[1] + areas[3]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Use slicing to print first 5 elements of areas list.
firstFive = areas[0:5]

# Use slicing to print last 5 elements of areas list.
lastFive =areas[10:4:-1]

# Print out downstairs and upstairs
print(firstFive)
print(lastFive)


# Quick check : What would be the output of this?
print(areas[10:5:-1])





