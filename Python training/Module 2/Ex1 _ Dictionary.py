
#######################################################################
# Getting to know the basics : Dictionary
#######################################################################
import operator

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = ''

# Use ind_ger to print out capital of Germany
print()

# From string in countries and capitals, create dictionary europe
europe = {'spain' : 'madrid', 'france' : 'paris', 'germany' : 'berlin', 'norway' : 'oslo'}

# Print europe
print(europe)
print('')
# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Adding values in a dictionary
europe['greece'] = 'athens'
print(europe)

# Deleting a value from a dictionary
del(europe['greece'])
print(europe)


# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'india' : {'capital':'New Delhi', 'population': 121.00} }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital' : 'rome', 'population' : 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# delete india from the dictionary as India is not in europe
del(europe['india'])
print('india deleted from europe: '+ str(europe))

# Print europe
print(europe)
print('')

# Methods in dictionaries
# clear method()
sampleDictionary = {'a':1, 'b':2, 'c':3, 'd':4}
sampleDictionary.clear()
print('Clear method: ' + str(sampleDictionary))
print('')

# fromkeys() method
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print('Dictionary with no values: ' + str(vowels))

value = 'vowel'
vowels = dict.fromkeys(keys, value)
print('Dictionary with values: ' + str(vowels))
print('')

# get() method
# You can also get the value like this with [] but this will throw an error in case there is no matching key
person = {'name': 'Phill', 'age': 22}
print('Name: ', person['name'])
print('')

person = {'name': 'Phill', 'age': 22}
print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))
print('')

# items() method
# random sales dictionary
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

items = person.items()
print('Original items:', items)
print('')

# keys()
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print('keys:' + str(person.keys()))

# values()
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print('values: ' + str(person.values()))
print('')

# setdefault()
person = {'name': 'Phill'}
# key is not in the dictionary
salary = person.setdefault('salary', 200)
print('person = ',person)
print('salary = ',salary)
print('')

# update()
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}
# adds element with key 3
d.update(d1)
print(d)

d = {'x': 2}
d.update(y = 3, z = 0)
print(d)
print('')

# sorting a dictionary by using a key
d = {1: 20, 3: 40, 4: 30, 2: 10, 0: 11}
print('Original dictionary : ',d)

# We are soring the keys here
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print(sorted_d)


#######################################################################
# Excercise
#######################################################################

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add the key 'italy' with the value 'rome' to europe.
europe1 = {'italy': 'rome'}
europe.update(europe1)


# Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
europe['poland'] = 'warsaw'


# Print europe
print(europe)

# Delete germany from the dictionary and print the keys and values
del(europe['germany'])

# Print europe
print(europe)

# use itemgetter to sort values of this dictionary
a = {'b':1, 'c':2, 'a':3, 'd':5}
Sorted_europe = sorted(europe.items(),key = operator.itemgetter(0))



# Add all three dictionaries in dict4, without using for loop. Hint: use update method
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
dic4.update(**dic1, **dic2, **dic3)
print(dic4)

