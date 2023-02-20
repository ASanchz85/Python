#Task:
'''
6 kyu
Find the missing letter
********************************************************************************************************
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
'''

import string

def find_missing_letter(chars):

    abc_l=string.ascii_lowercase
    abc_u=string.ascii_uppercase
    lower_case=True
    to_number=list()
    
    for letter in chars:
        if letter in abc_l:
            to_number.append(abc_l.index(letter))
        elif letter in abc_u: 
            to_number.append(abc_u.index(letter))
            lower_case=False
        else : return ('wrong input')
    
    for i in range(len(to_number) - 1):
        if to_number[i + 1] - to_number[i] != 1:
            if lower_case : return abc_l[to_number[i] + 1]
            else : return abc_u[to_number[i] + 1]
            

#
'''
passed
'''