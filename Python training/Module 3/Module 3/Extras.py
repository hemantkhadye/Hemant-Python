import pandas as pd

inFile = pd.read_csv('iris.csv')
print(inFile.head(5))


nums = (1,2,3)
num1, num2, num3 = nums
print(num1, num2, num3)

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: species_count
    species_count = {}

    # Extract column from DataFrame: col
    col = inFile['Species']
    print(col)

    # Iterate over species column in DataFrame
    for cl in col:
        if cl in species_count.keys():
            # If the species is in species_count, add 1
            species_count[cl] += 1
        else:
            # Else add the species to species_count, set the value to 1
            species_count[cl] = 1

    # Return the species_count dictionary
    return species_count


# Call count_entries(): result
result = count_entries(inFile, 'Species')

# Print the result
print(result)