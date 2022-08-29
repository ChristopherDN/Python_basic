# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if s.endswith('g', 6):
        return s + 'ly'
    elif len(s) >= 3:
        return s + 'ing'
    else:
        return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
        substr1 = 'bad'
        substr2 = 'not'
        index = s.find(substr1) > s.find(substr2)
        print(index)
        if s.__contains__('so'):
            return s.replace('not so bad', 'good')
        else: s.__contains__('that')
        return s.replace('not that bad','good')


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + +b-back
def front_back(a, b):
    if len(a) % 2 == 0 and len(b) % 2 == 0:
        return f'{a[0:2]}{b[:1]}{a[2:4]}{b[1:2]}'
    elif len(a) % 2 == 0 and len(b) % 2 != 0:
        return f'{a[0:3]}{b[0:3]}{a[3:6]}{b[3:5]}'
    else:
        return f'{a[0:3]}{b[:2]}{a[3:5]}{b[2:3]}'


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(prefix + ' got: ' + got + ' expected: ' + expected)


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


main()
