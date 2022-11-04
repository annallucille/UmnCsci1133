

###### Problem (1) ######
'''
 Write a function new_cases(date, state) that takes in two strings representing a date and 
 a two-letter state abbreviation, and returns an integer representing the number of new cases 
 reported by the given state on that date.  If there is no row in the file with the given state/date 
 combination, the function should instead return -1.
'''
def new_cases(date,state):
    file = open('covid_data.csv')
    new_cases = -1
    for line in file:
        new_line = line.split(',')
        if state == new_line[1] and date == new_line[0]:
            new_cases = new_line[5]
    file.close()
    return int(new_cases)



###### Problem (2) ######
'''
 Write a function length_correct(fname, length) that takes in a string and an integer, and returns None. 
 fname will be a name of a file stored as a string, and length will be the max length of any line in the file.  
 You may assume for this problem that the filename given is a real file in the same folder as hw08.py.
 The function should produce a new file “mod-<fname>” (where <fname> is replaced by the value of fname). 

 This new file should contain the same content of “fname” but modified in the following way:
  - Each line of the file in fname which has a length less than or equal to length 
    should be written unmodified to the new file.
  - If a line has a length of greater than length, that line should be written as two separate lines 
    in the modified file, with length - 1 characters appearing on the first line and ending with a \n character, 
    and the remaining characters on the line below it.  
  - If the remaining characters also have a length greater than length, you need to split that line as well.  
 This process continues until the remaining characters can fit into one line.
'''

def length_correct(fname,length):
    file = open(fname)
    txt = []
    copy = open(f"mod-{fname}", 'w+')
    for line in file:
        line_length = len(line)
        string = line.split('\n')
        if line_length <= length: 
            txt.append(string[0])
        elif line_length> length:
            i = int(line_length/length)
            j = 0 
        while j <= i:
            line1=line[(length-1)*j:(length-1)*(j+1)]
            string1 = line1.split('\n')
            txt.append(string1[0])
            j+=1
    txt_string = '\n'.join(txt)
    copy.write(txt_string)
    file.close()
    copy.close()


###### Problem (3) ######
'''
 Write a function stretch_model(fname_in, fname_out) that reads all the vertices and faces in the 
 OBJ file specified by the string fname_in.  The function should then transform the vertices to 
 stretch the model by a factor of 2 along the y-axis, and then save the transformed vertices and 
 faces to a file specified by the string fname_out.  This function should return the total number of 
 vertices that were stretched.  
'''

def stretch_model(fname_in, fname_out):
    try: 
        file = open(fname_in)
        file_out = open(fname_out, 'w')
        i =0 
        for line in file:
            string = line.split(' ')
            if string[0] == 'v':
               string[2]=str(float(string[2])*2)            
               line1 = ' '.join(string)
               file_out.write(line1)
               if string[2] != '0.0':
                    i+=1
            else:
                file_out.write(line)
        return i 
    except:
        return -1





###############################

def convert_csv(fname):
    file = open(fname, 'r')
    txt = []
    for line in file:
        txt.append(line)
    name = fname.split('.')
    convertFile= open(f"{name[0]}.txt", 'w')
    for line in txt:
        convertFile.write(line)
        
def copy_file(fname):
    file = open(fname, 'r')
    txt = []
    for line in file:
        txt.append(line)
    convertFile= open(f"mod_{fname}", 'w')
    for line in txt:
        convertFile.write(line) 