
############################################ Warm Up ###############################################


### Problem (1) ###
'''
Type out a step by step sequence, similar to what's shown above for fact_recursion(5), 
for what would happen if you called mystery([5, 3, 7]).  You may want to consider putting in some print statements 
and running the function to ensure you're on the right track.  Remember that lst[1:] makes a copy of lst with the 
first element removed.
'''

def mystery(lst):
    if lst == []:
        return []
    else:
        return [lst[0]-5] + mystery(lst[1:])
    
    # mystery([3,5,7]) -> [3-5] + mystery([5,7])
    ## mystery([5,7]) -> [5-5] + mystery([7])
    ### mystery([7]) -> [7-5] + mystery([])
    ## mystery([5,7]) -> [5-5] + [7-5]
    # mystery([3,5,7]) -> [3-5] + [5-5] + [7-5] = [-2, 0, 2]

'''
What does this function do, in a single sentence?
'''
    # It takes a list and returns a new list where each value is 5 less than it was
    
'''
What is the base case?
'''
    # The empty list
    
'''
Does the recursive case (also called the reduction step) always move towards the base case?  Explain why or why not.
'''
    # yes, the list always ends up empty 
    
'''
Write an equivalent function using a loop rather than recursion.
'''
def mystery_loop(lst):
    for i in range(len(lst)):
        lst[i] -= 5
    return lst

### Problem (2) ###
'''
Follow the prompts below to write a recursive function to determine the sum of a list of integers.
'''

def sum_list(vals):
    if vals == []:
        return []
    else:
        return vals[0] + sum_list(vals[1:])
    
    
    # sum([3,5,7]) -> 3 + sum([5,7])
    ## sum([5,7]) -> 5 + sum([7])
    ### sum([7]) -> 7 + sum([])
    ## sum([5,7]) -> 5 + 7
    # sum([3,5,7]) -> 3 + 5 + 7 = 15
    
    
    
### Problem (3) ###
'''
Construct a recursive function to return a string in its reverse order on the console. 
'''
def reverse_string(st):
    if st == '':
        return ''
    else:
        return reverse_string(st[1:]) + st[0]
  
  
    # reverse_string('hello') -> reverse_string('ello') + 'h'
    ## reverse_string('ello') -> reverse_string('llo') + 'e'
    ### reverse_string('llo') -> reverse_string('lo') + 'l'
    #### reverse_string('lo') -> reverse_string('o') + 'l'
    ##### reverse_string('o') -> reverse_string('') + 'o'
    #### reverse_string('lo') -> 'o' + 'l'
    ### reverse_string('llo') -> 'o' + 'l' + 'l'
    ## reverse_string('ello') -> 'o' + 'l' + 'l' + 'e'
    # reverse_string('hello') -> 'o' + 'l' + 'l' + 'e' + 'h'
    
    
    
######################################## Stretch #############################################

### Problem (1) ###
'''
Construct a recursive function named fibonacci that will take an integer value n as an argument and return Fn.
'''

def fibonacci(n):
    if n== 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
### Problem (2) ###        
'''
Write a recursive function double_reverse(str_list) that takes in a list of strings and returns a new 
list which has all of the original strings reversed, in reverse order.  
'''

def double_reverse(str_list):
    if str_list == []:
        return []
    else:
        return double_reverse(str_list[1:]) + [reverse_string(str_list[0])]
            
            
            
############################################ Work Out ##################################################

### Problem (1) ###
'''
Write a recursive function deep_square that takes in a list and will go through a nested list of integers, 
and then return the squared result of each integer, preserving the nested list structure.
'''

def deep_square(lst):
    if lst == []:
        return []
    else: 
        if type(lst[0]) == int:
            return [lst[0]**2] + deep_square(lst[1:])
        else:
            return [deep_square(lst[0])] + deep_square(lst[1:])
        
### Problem (2) ###
'''
Write a recursive function flat_square that takes in a nested list and returns the squared 
result of each integer in a flattened list. 
'''

def flat_square(lst):
    if lst == []:
        return []
    else: 
        if type(lst[0]) == int:
            return [lst[0]**2] + flat_square(lst[1:])
        else:
            return flat_square(lst[0]) + flat_square(lst[1:])