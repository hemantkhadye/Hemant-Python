
#######################################################################
# Getting to know the basics : Scope
#######################################################################

# Create a string: team
team = "Eclerx"

# Global variables
# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = 'newEclerx'
# Print team
print('Initial value: ' + str(team))

# Call change_team()
change_team()

# Print team
print('Changed value: ' + str(team))
print('')

#################################################################
# Nested functions
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    def test(a):
        return a


    # Return inner_echo
    return(inner_echo)

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
print('')

#################################################################
# More than one nested functions
def foo(x,y):
    def do_this(a,b):
        print(a+b)
    def do_that(c,d):
        print(c*d)
    # do_this(x,y)
    # do_that(x,y)
    foo.do_this = do_this
    foo.do_that = do_that


foo(10, 20)
foo.do_this(1,2)
foo.do_that(4,5)
print('')


# Declaring global using nonlocal
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""

    # Concatenate word with itself: echo_word
    echo_word = word + word
    # Print echo_word
    print(echo_word)

    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        # Use echo_word in nonlocal scope
        nonlocal echo_word

        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'

    # Call function shout()
    shout()

    # Print echo_word
    print(echo_word)


# Call function echo_shout() with argument 'hello'
def eco_shout(text, echo= 1):
    print(text*echo)
echo_shout('hello')