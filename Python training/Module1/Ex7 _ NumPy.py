
#######################################################################
# Getting to know the basics : NumPy
#######################################################################

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# height is available as a regular list

height = [1.8, 1.6, 2, 1.8, 2.2]
# Create a Numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height*.0254

# Print np_height_m
print(np_height_m)


weight = [58, 67, 72, 55, 63]
# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * .453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m ** 2

# Print out bmi
print(bmi)



#######################################################################
# Excercise
#######################################################################

# convert two list into numpy array and add both of them

a = [1,2,3,4,5]
b = [6,7,8,9,10]

num_a =np.array(a)
num_b = np.array(b)
num_c = num_a + num_b
print(num_c)