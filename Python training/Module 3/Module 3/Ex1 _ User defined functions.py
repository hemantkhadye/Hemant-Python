
#######################################################################
# Getting to know the basics : Pandas
#######################################################################

import pandas as pd

# Define the function stringConcat
def stringConcat():
    """This the docstring for function stringConcat"""
    # Concatenate the string: word
    word = 'congratulations' + '!!!'

    print(word)

# Function with single parameter
def anyStringConcat(word):

    word = word + '!!!'

    print(word)

# Function calling
var1 = anyStringConcat('Hi')
print('Because print does not return any values: ' + str(var1))

# Returning value
def anyStringConcat(word):

    word = word + '!!!'

    return word

var2 = anyStringConcat('Hello')
print('Single value returned: '+ str(var2))

# Functions with multiple arguments

def multipleArgs(list1, list2):
    """Pass two lists to this function and concat both of them, finally print the new list"""
    for a in list1:
        print(a)
    for b in list2:
        print(b)

    new = list1 + list2
    print(new)
    print('')
    return(new)

a = [1,2,3]
b = [4,5,6]

c = multipleArgs(a, b)
print('Value of c is here: ' + str(c))
print('')


# name = input('Please enter your name? \n')
# print('Hi '+ name + ' ,how are you?')


#################################################################

# Functions with pre-set parameters
# Define shout_echo
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1*echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo('Hey', 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)
print('')

# Define shout_echo
def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', 5, True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey', intense = True)

# Print values
print(with_big_echo)
print(big_no_echo)
print('')


#################################################################
# *args

def test(*args):
    print('Your args value: ' + str(args))

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    print(hodgepodge)


a = ['a','b', 'c', 'd', 'e']
gibberish(*a)

# kwargs
def report_status(**kwargs):
    """Print out the status of a movie character."""

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

cat = ['a','b', 'c', 'd', 'e']
prices = [10, 20, 30 ,40, 50]
for c in cat:
    index = prices[cat.index(c)]
    report_status(cat = c, prices = str(index))



print('')

#######################################################################
# Exercise
#######################################################################

# Build a function that prints out 10 numbers using for loop. Name it anything you want. It will be a function without any parameters
def Loop10():
    for i in range(1, 11):
        print(i)

Loop10()
# Build a function that prints as many numbers we want in for loop. This function will have one argument n as total numbers that need to be printed
def ULoop(num):
    for i in range(0, num+1):
        print(i)

ULoop(15)
# Build a function that uses while loop and prints numbers less than 20. Name it anything you want
def condLoop():
    i = 0
    while(i < 20):
        print(i)
        i+=1


condLoop()


# Build a function than calculates the sum of n number of terms
def SumArgs(*args):
    addNum = 0
    for n in args:
        addNum = addNum + n
    print(addNum)
    print(sum(args))

SumArgs(1,45,2,6,88,55,22,2,36)




