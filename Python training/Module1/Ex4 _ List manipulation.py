
#######################################################################
# Getting to know the basics : List Manipulation
#######################################################################

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[9] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

print(areas)
print(areas_1)
print(areas_2)

# Deleting values from a list
del areas[2:]
print(areas)

# Copying a list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_ShallowCopy = areas
# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
print(areas_copy)

# Checking an element in a list
print(9.5 in areas)

#######################################################################
# Excercise
#######################################################################

# Change the value of furst 2 elements in one line of code. Remember to use slicing - areas[:endpoint] = [value1, value2]
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas[:2] = [20, 31]
print(areas)


# Print area of hallway
areas = [["hallway", 11.25], ["kitchen", 18.0], ["living room", 20.0], ["bedroom", 10.75], ["bathroom", 9.50]]
print(areas[0][1])


# Quick check : What would be the output if I add two lists?
a = [1, 2, 3]
b = [4, 5, 6]

print(a+b)

