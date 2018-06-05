
#######################################################################
# Getting to know the basics : Variables & Types
#######################################################################

# Type string
city = 'Pune'
print(city +' : '+ str(type(city)))

# Type int
number = 10

print(str(number) +' : '+ str(type(number)))

# Type float
height = 182.3
print(str(height) +' : '+ str(type(height)))

# Type boolean
bool = True
print(bool)

a = 10
b = 20
c = 30

print(max(a,b,c))

Sum = a + b + c
print(Sum)


#######################################################################
# Excercise
#######################################################################

# What would be the mean of a,b,c? You have already calculated the Sum of 3 numbers in the code above.
mean =(a + b + c) / 3
print(mean)

# What would be the output if I multiply strings?
s1 = 'Hi'
s2 = 'Hello'
s3 = 'Greetings'

print()


# Quick check : What would be the output?

s1 = 'Hi'
s2 = 'Hello'
s3 = 'Greetings'

print(max(s1))
print(max(s1,s2,s3))
