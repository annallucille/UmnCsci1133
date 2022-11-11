
###### Warm up ######

# Problem (1)


ms = 'mississippi'
count = ms.count('s')
print(count)

# Problem (2)

ox = ms.replace('iss', 'ox')
print(ox)

# Problem (3)

pCount = ms.count('p')
print(pCount)
print(len(ms))

# Problem (4)

def foo(istring):
    '''
    Tzakes a string and for every character not in p, it adds to os
    '''
    p = '0123456789'
    os = ''
    for ch in istring:
        if ch not in p:
            os += ch
    return os


# Problem (5)

def foo_two(istring):
    p = '0123456789'
    os = ''
    for i in range(len(istring)):
        if istring[i] not in p:
            os += istring[i]
    return os



###### Stretch ######

'''
Problem (1)

Write a Python program that prompts the user to enter a sequence of 
lowercase words and stores in a list only those words whose first letter occurs again 
elsewhere in the word
'''

def more_letters(string):
    string = str(input('Enter a word '))
    same = []
    while string != '':
        for i in range(1, len(string)):
            if string[i] == string[0]:
                same.append(string)
        string = str(input('Enter a word '))
    return same

'''
Problem (2)

Write a function named is_palindrome that will take a single string argument and return True if the argument is a palindrome
'''

def is_palindrome(string):
    if len(string)%2 == 0:
        for i in range(int(len(string)/2)):
            if string[i] != string[-(i+1)]:
                return False
    return True



###### Work out ######

'''
Problem (1)

Write a function called igpay(word) that takes in a string word representing a word in English, 
and returns the word translated into Pig Latin.
'''

def igpay(word):
    vowels = ['a','e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i] in vowels:
            pig = word[i:len(word)] + word[0:(i-1)] + 'ay'
    return pig

