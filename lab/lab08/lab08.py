import csv
import random

####### Warm Up #######

'''
Problem (1) 

 Write a function wordcount(fname)which takes in a string fname, 
 opens the file at location fname, counts the number of words in the 
 file and returns that number. Assume that “words” here refers to any 
 sequence of one or more consecutive non-whitespace characters.  
'''

def wordcount(fname):
    try: 
        data = fname.read()
        words = data.split()
        return words
    except FileNotFoundError: 
        return 'invalid file'

'''
Problem (2)

Try except 
'''


####### Stretch #######

'''
Problem (1)

 Write a Python function  make_data(fname)which takes in a string fname representing the name 
 of a file (including the extension, which you can assume will be .csv).  
 The function should create a CSV (comma separated value) file with the specified row,
 that has 1000 lines of data, and return nothing.  Each line will contain 2 values: the line number 
 (starting with 1) and a randomly generated integer value in the closed interval [-1000, 1000].  
 For example, the first few lines might look like this:
'''

def make_data(fname):
    file=open(fname, 'a')
    for j in range(0,1000):
        file=open(fname, 'a')
        file.write(str(j))
        file.write(',')
        file.write(str(random.randint(-1000,1000)))
        file.write('\n')
        file.close() 
        
'''
Problem (2)

 Write a second function  read_data(fname)that will read the file created in the previous 
 problem using a for loop and print out the minimum and maximum randomly generated values in 
 the file (the function should return nothing). Again, you should not import/use the Python 
 csv module. 
'''

def read_data(fname):
    file=open(fname)
    line1 = 0
    line2 = 0
    for line in file:
        number = line.split(',')
        if int(number[1])> line1:
            line1 = int(number[1])
        elif int(number[1]) < line2:
            line2 = int(number[1])
    print(line1)
    print(line2)
    
    
####### Workout #######

def average(fname):
    file = open(fname,'r')
    sumStocks = 0
    i =0 
    for line in file: 
        number = line.split(',')
        if number[4] != 'Close':
            sumStocks+=float(number[4])
            i+=1
    avg = sumStocks/i
    return avg

def max(fname): 
    file=open(fname)
    line1 = 0
    for line in file:
        number = line.split(',')
        if number[4] != 'Close':
            if float(number[4])> line1:
                line1 = float(number[4])
    return line1

def min(fname):
    file=open(fname)
    for line in file:
        number = line.split(',')
        if number[4] != 'Close':
            line2 = float(number[4])
            if float(number[4]) <= line2:
                line2 = float(number[4])
    return line2
    
def median(fname):
    file = open(fname)
    txt =[]
    for line in file:
        number = line.split(',')
        if number[4] != 'Close':
            txt.append(number[4])
    i = int(len(file.readlines())/2)
    return txt[i]


def min_and_max_stock_prices(fname):
    file = open(fname, 'r')
    txt = []
    for line in file:
        txt.append(line)
    name = fname.split('.')
    convertFile= open(f"{name[0]}.txt", 'w')
    for line in txt:
        convertFile.write(line)
    x = max(f"{name[0]}.txt")
    y = min(f"{name[0]}.txt")
    z = average(f"{name[0]}.txt")
    a = median(f"{name[0]}.txt")
    print(x, 'highest closing value')
    print(y, 'lowest closing value')
    print(z, 'is the average')
    print(a, 'is the median')
    
    
