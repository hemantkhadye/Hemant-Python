
#######################################################################
# Getting to know the basics : Pandas
#######################################################################
# Import pandas as pd
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drivesLeft = [True, False, False, False, True, True, True]
carsPerThousand = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': drivesLeft, 'cars_per_thousand': carsPerThousand}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
print('')

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
print('')

# Select a column
print(cars[['country', 'cars_per_thousand']])
print('')

# Slicing a dataframe
print(cars[0:4])
