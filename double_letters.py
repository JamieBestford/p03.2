"""
Problem:

    The function 'doubler' takes a word as input.  It should create and print
    a string, where each character in the string is doubled, for example:

    "test" -> "tteesstt"

Tests:

    >>> doubler("test")
    tteesstt
    >>> doubler("original")
    oorriiggiinnaall
    >>> doubler("hihihi")
    hhiihhiihhii

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def doubler(word):

    new_word = ""

    for chara in word:

        new_word = new_word + chara * 2

    print(new_word)



#~~~~~~~~~#
#Completed#
#~~~~~~~~~#
        

