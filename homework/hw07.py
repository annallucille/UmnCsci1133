# Homework 07

###### Problem (A) ######

'''
Write a function starting_string(str_one, str_two) that takes in two strings, 
and returns the common substring that begins each string.  
If the two strings do not begin with a common substring, return an empty string. 
'''

def starting_string(str1, str2):
    '''
    Purpose:
      return a string that is contained in the beginning of two strings
    Input Parameter(s):
      two strings
    Return Value:
      A string, could be the empty string
    '''
    newstr = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            newstr += str1[i]
        else:
            return newstr
    return newstr


###### Priblem (B) #######

'''
Write a function find_substring(string, substring) that takes in two strings, 
where string is some string, and substring represents a string contained in string. 
The function must return a list of all the locations where the substring is found in string
'''

def find_substring(string, substring):
    '''
    Purpose:
      return indexes where the substring is found
    Input Parameter(s):
      two strings
    Return Value:
      A list of indexes
    '''
    index = []
    for i in range(len(string)):
        if  string[i:i+len(substring)]== substring:
            index.append(i)
    return index


###### Problem (C) ######

'''
Write a function build_csv_string(data) that takes in a list data. 
data will be a list of lists, where each sub list is of length 1, 2, or 3.  
  - Length 1 lists will contain a name (as a string). 
  - Length 2 lists will contain a name and an assignment title (as a string). 
  - Length 3 lists will contain a name, an assignment title, and a score (as a float or int).  

'''

def build_csv_string(data):
    filestr='name,assignment,grade'
    for i in range(len(data)):
        if len(data[i])== 1:
            data[i].append('N/A')
        if len(data[i]) == 2:
            data[i].append(0)
        filestr+='\n'
        filestr += data[i][0]
        filestr +=','
        filestr+= data[i][1]
        filestr += ','
        filestr+=str(data[i][2])
    return filestr