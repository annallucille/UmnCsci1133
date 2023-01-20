

################# Problem (A) ###################
'''
For problem A you will be writing two different functions to iterate through a string. 
One function will use recursion and the other will use a loop. Write two functions rec_sum_digits 
and loop_sum_digits both of which accept a single string argument st.

Both functions should return an integer representing the sum of all of the digits in the string.  
If there are no digits in the string the function should return 0.  You are permitted to use the string method 
.isdigit() to check whether a given character is a digit.
'''

def loop_sum_digits(st):
    digit_sum = 0 
    ls = [*st]
    for char in ls:
            if char.isdigit():
                digit_sum += int(char)
    return digit_sum
                
def rec_sum_digits(st):
    ls = [*st]
    if ls == []:
        return 0
    elif ls[0].isdigit():
        new_st = ''.join(ls[1:])
        return int(ls[0]) + rec_sum_digits(new_st)
    else:
        new_st = ''.join(ls[1:])
        return rec_sum_digits(new_st)
    

################## Problem (B) ###################
'''
The Collatz conjecture is an unproven mathematical rule that says the following:

Take any positive integer n. If n is even, divide it by 2 to get n/2 
(use integer division so that you don't end up with floating point numbers). 
If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process indefinitely, 
and eventually you will reach 1.

Write a recursive function called collatz that takes in a single positive integer argument n 
and returns the list of numbers in the collatz sequence from n to 1, inclusive.
'''

def collatz(number):
    if number == 1:
        return [1]
    elif number % 2 ==0:
        return [number]+collatz(int(number/2))
    else:
        return [number]+collatz((3*number)+1) 

    
################## Problem (C) ###################
'''
Write a function collect_words which will accept a single argument collection. 
collection will be of type str, int, float, list, or tuple. The function should return a 
list of all of the strings contained within the collection. This means that:
 - If collection is an int or float, an empty list should be returned. 
 - If collection is a string, a list with a single element should be returned. 
 - If collection is a tuple or a list, a list should be returned with all of the strings 
   contained within any level of collection regardless of nesting depth.
'''

def collect_words(collection):
    if collection == [] or collection == ():
        return []
    elif type(collection) == list:
        return collect_words(collection[0]) + collect_words(collection[1:])
    elif type(collection) == tuple:
        return collect_words(collection[0]) + collect_words(collection[1:])
    elif type(collection) == str:
        return [collection]
    else:
        return []