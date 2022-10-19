import copy
from email.mime import image
import random

'''
Anna Breck
CSCI 1133
Homework 6
'''

# Problem (A)
#   implementing the invert function

def invert(img_matrix):
    '''
    Purpose:
      Inverts the colors in an image by setting each color component to
      255 minus its original value.
    Input Parameter(s):
      A 3D matrix (list of lists of lists) representing an .bmp image
      Each element of the matrix represents one row of pixels in the image
      Each element of a row represents a single pixel in the image
      Each pixel is represented by a list of three numbers between 0 and 255
      in the order [red, green, blue]
    Return Value:
      A 3D matrix of the same dimensions, with the colors of each pixel inverted
    '''
    for y in range(len(img_matrix)):
        for x in range(len(img_matrix[0])):
            for i in range(3):
                img_matrix[y][x][i]=255-img_matrix[y][x][i]
    return img_matrix
        
# Problem (B)
#   implementing the high_contrast function.
def high_contrast(img_matrix):
    '''
    Purpose:
      For every pixel, sets each color component to 0 (if the original
      value was 127 or less), or 255 (if the original value was >= 128).
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, with high-contrast colors
      as described above.
    '''
    for y in range(len(img_matrix)):
        for x in range(len(img_matrix[0])):
            for i in range(3):
                if img_matrix[y][x][i]>127:
                    img_matrix[y][x][i] = 255
                else:
                    img_matrix[y][x][i] = 0
    return img_matrix
                
# Problem (C)
#   implementing the rotate_quadrants function  
def rotate_quadrants(img_matrix):
    '''
    Purpose:
      Split the image into four equally sized quadrants, and rotate
      them clockwise to form the output image.
    Input Parameter(s):
      (see invert) - plus, it can be assumed the img_matrix will have
      an even number of rows and columns.
    Return Value:
      A 3D matrix of the same dimensions, where each pixel has been moved
      to the corresponding location.'''
      
    img_copy = copy.deepcopy(img_matrix)
    height = int(len(img_matrix)/2)
    width = int(len(img_matrix[0])/2)
    for n in range(height):
        for i in range(width):
            img_copy[n][i]=img_matrix[n+height][i]
    for n in range(height, len(img_matrix)):
        for i in range(width):
            img_copy[n][i]=img_matrix[n][i+width]
    for n in range(height, len(img_matrix)):
        for i in range(width, len(img_matrix[0])):
            img_copy[n][i]=img_matrix[n-height][i]
    for n in range(height):
        for i in range(width,len(img_matrix[0])):
            img_copy[n][i]=img_matrix[n][i-width]           
    return img_copy         
            
# Problem (D)
             
def custom_filter(img_matrix):
    '''
    Purpose:
      im not exactly sure, just kinda messes it up (im making computer art good sir)
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    colors = []
    for i in range(255):
        colors.append(i)
    for y in range(len(img_matrix)):
        for x in range(len(img_matrix[0])):
            if sum(img_matrix[y][x]) >=150 and sum(img_matrix[y][x])<=700:
                if img_matrix[y][x][0] < 200:
                    img_matrix[y][x][0]=random.choice(colors)
                if img_matrix[y][x][1] < 200:
                    img_matrix[y][x][1]=random.choice(colors)
                if img_matrix[y][x][2] < 200:
                    img_matrix[y][x][2]=random.choice(colors)
            elif sum(img_matrix[y][x])> 700:
                for i in range(3):
                    img_matrix[y][x][i]=255
            else:
                for i in range(3):
                    img_matrix[y][x][i]=0
    return img_matrix




#--------------------------------------------------
# DO NOT EDIT ANYTHING BELOW THIS LINE
# .bmp file manipulation functions.  You don't have to understand these.
#--------------------------------------------------

def big_end_to_int(ls):
    '''
    Byte conversion helper 
    Purpose:
      Compute the integer represented by a sequence of bytes
    Input Parameter(s):
      A list of bytes (integers between 0 and 255), in big-endian order
    Return Value:
      Integer value that the bytes represent
    '''
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

def transform_image(fname,operation):
    '''
    .bmp conversion function
    Purpose:
      Turns a .bmp file into a matrix of pixel values, performs an operation
      on it, and then converts it back into a new .bmp file
    Input Parameter(s):
      fname, a string representing a file name in the current directory
      operation, a string representing the operation to be performed on the
      image. 
    Return Value:
      None
    '''
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [red,green,blue].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i+2],data[i+1],data[i]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()

    #Perform operation on the pixel matrix
    if operation == 'invert':
        new_matrix = invert(matrix[::-1])
    elif operation == 'high_contrast':
        new_matrix = high_contrast(matrix[::-1])
    elif operation == 'custom_filter':
        new_matrix = custom_filter(matrix[::-1])
    elif operation == 'rotate_quadrants':
        new_matrix = rotate_quadrants(matrix[::-1])
    else:
        return
    new_matrix = new_matrix[::-1]
    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i+2],data[i+1],data[i] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()



