'''
Anna Breck
CSCI 1133
Homework 5
'''

'''
Problem (A)
'''

def longest_even(shows):
    longest = '0'
    for show in shows:
        if len(show) % 2==0 and len(show)>len(longest):
            longest = show
    return longest

'''
Problem (B)
'''
def prior_to(data, key):
    message = []
    i = 0
    for num in data:
        if num == key:
            n = data.index(num,i)
            message.append(data[n-1])
        i += 1
    return message 

'''
Problem (C)
'''
def all_three(social, grades, sleep):
    darkMagic = []
    for name in social:
        if name in grades and name in sleep:
            darkMagic.append(name)
    return darkMagic