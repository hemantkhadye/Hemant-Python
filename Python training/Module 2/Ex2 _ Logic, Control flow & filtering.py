
#######################################################################
# Getting to know the basics : Logic, Control flow
#######################################################################
import numpy as np

# Comparison of integers
x = -3 * 6

# Comparison of strings
y = "test"

# Comparison of booleans
print(x >= -10)
print("test" <= y)
print(True > False)


mh = [18.0, 20.0, 10.75, 9.50]
# print(mh[mh>=18])

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print('My house: ' + str(my_house[my_house >= 18]))
print('')

# my_house less than your_house
print('These areas are smaller than your_house list: ' + str(my_house[my_house < your_house]))
print('')

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)

# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# Finding the index based on a condition
print('Indexing for or condition: ' + str(np.where(np.logical_or(my_house > 18.5, my_house < 10))))
print('Indexing for and condition: ' + str(np.where(np.logical_and(my_house < 11, your_house < 11))))



#######################################################################
# Excercise
#######################################################################

# Subset areas which are greater than equal to 13, in both the lists

my_house = np.array([18.0, 20.0, 10.75, 9.50, 19, 50, 64])
your_house = np.array([14.0, 24.0, 14.25, 9.0, 16, 23, 12])
print(str(my_house[my_house >= 13]), str(your_house[your_house >= 13]))


# Use logical_or to find the index where:
# Condition : my_house greater than 15 or your_house less than 20 or my_house less than 9. You have in total 3 conditions

print(str(np.where(np.logical_or(my_house > 15, your_house < 20, my_house < 9))))

# Use logical_and to find the index where:
# Condition : my_house < 20 and your_house < 18
print(str(np.where(np.logical_and(my_house < 20, your_house < 18))))



