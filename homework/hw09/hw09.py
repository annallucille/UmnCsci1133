import random
import string

###### Problem (A) ######
'''
Create a function weighted_choice that takes as a parameter a dictionary of words and their corresponding counts. 
The function should randomly choose one of the words, using the counts as weights in the selection.
'''

def weighted_choice(dict):
    lst = []
    for word in dict:
        x = dict[word]
        for i in range(x):
            lst.append(word)
    return random.choice(lst)

###### Problem (B) ######
'''
Write a function that count_votes(district, office) that takes in two strings as parameters. 
  - district should be the name of a file containing all voting data for a given district, in the format specified above.  
    You can assume that said file actually exists (no need for a try-except block).
  - office should be the name of one of the column titles present in the CSV file.  
    You can assume that the office passed in will match one of the columns in the CSV file.  
The function should return a dictionary in which each key is a name present in the column 
corresponding to the given office, and the value represents how many times that name occurs within the column.
'''

def count_votes(district, office):
    votes = {}
    fp = open(district)
    first_line = fp.readline()
    first_string = first_line.rstrip('\n')
    first_list = first_string.split(',')
    for word in first_list:
        if word == office:
            i = first_list.index(word)
    for line in fp:
        string = line.rstrip('\n')
        lst = string.split(',')
        if lst[i] in votes:
            votes[lst[i]] += 1
        else:
            votes[lst[i]] = 1
    fp.close()
    return votes

###### Problem (C) ######

'''
Write a function called random_sent(source_file, length) that takes in two parameters:
  - source_file is a string representing the name of a file in the current directory, 
    which we'll use as a basis for producing our text
  - length is an integer representing the number of words in our output text
'''

def random_sent(source_file, length):
    dict = {}
    next_word = {}
    random_lst = []
    fp = open(source_file)
    for line in fp: 
        string1 = line.rstrip('\n') 
        string1 = string1.translate(str.maketrans('', '', string.punctuation))
        lst = string1.split(' ')
        for word in lst:
            i = lst.index(word)+1
            if word in next_word and i < len(lst):
                next_word[word]+= [lst[i]]
            elif word not in next_word and i < len(lst): 
                next_word[word] = [lst[i]]
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    for z in range(length):
        if len(random_lst) == 0:
            random_lst.append(weighted_choice(dict))
        elif random_lst[z-1] in next_word:
            random_lst.append(random.choice(next_word[random_lst[z-1]]))
        else:
            random_lst.append(weighted_choice(dict))
    random_str = ' '.join(random_lst)
    fp.close()
    return random_str