

'''
Anna Breck
CSCI 1133
Homework 4
'''

'''
Problem (A)
 Write a function called sum_odd_digits(a_number) that takes in one parameter a_number, which represents a positive integer.
 Calculate and return the sum of all of the odd digits which make up the given number.
'''

def sum_odd_digits(a_number):
    if a_number <=0:
        return 'Error, negative or 0'
    num= str(a_number)
    sum=0 
    for x in num:
        if int(x) %2 != 0:
            sum += int(x)
    return sum

'''
Problem (B)
 Write a function next_divisor(n, lower_bound), that takes in two non-negative int values.  
 n is the number you will search for a divisor of, and lower_bound will also be an integer. 
 The function next_divisor should return the smallest divisor which is greater than lower_bound. 
 If no such integer exists, return -1. You cannot assume that the first argument will be larger than the second.
'''

def next_divisor(n, lb):
    if n < lb:
        return -1
    for i in range(lb+1,n):
        if  n%i == 0:
            return i 



'''
Problem (C)
 For this problem you will be implementing a version of the mathematical strategy game 
 Nim, said to have originated in China. You will write a function play_nim(winning_number) 
 which will return either the integer 1 or 2, indicating whether player one or player two has won the game. 
 winning_number will be a positive integer, representing the goal number. 
 When the function is called, a game of Nim will begin. Starting with zero, players one and two will be 
 alternatingly prompted for a number between 1 and 3. The number that players input will be added to the 
 current count. The player who causes the count to become equal to or greater than the winning_number wins. 
 If player one wins the integer 1 will be returned, and if player two wins the integer 2 will be returned. 

'''

def play_nim(winning_number):
    sum = 0
    p1 = 0 
    p2 = 0 
    winner = 0
    while sum < winning_number:
        print('Current Score', sum, end = '. ')
        p1 = int(input('Player 1 enter a number:' ))
        while p1 not in range(1,4):
            print('Invalid number, try again.')
            print('Current Score', sum, end = '. ')
            p1 = int(input('Player 1 enter a number:' ))
        sum += p1
        winner =1 
        if sum >= winning_number:
            return winner 
        print('Current Score', sum, end = '. ')   
        p2 = int(input('Player 2 enter a number:' ))
        while p2 not in range(1,4):
            print('Invalid number, try again.')
            print('Current Score', sum, end = '. ')
            p2 = int(input('Player 2 enter a number:' ))
        sum += p2
        winner = 2
    return winner
            
