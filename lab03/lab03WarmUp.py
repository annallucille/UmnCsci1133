import turtle 


# (2) drawing a square function 
def draw_square(length):
    n=0
    while n<5: 
        turtle.forward(length)
        turtle.left(90)
        n+=1
   
# (3) drwing a triangle function 
def draw_triangle(length):
    n=0
    while n<4: 
        turtle.forward(length)
        turtle.left(120)
        n+=1
 
# (4) Shape selection       
def shape_choice(shape):
    if (shape == "T" or shape == "t" or shape == 'Triangle' or shape == 'triangle'):
        triangleSide = int(input('Triangle side length: '))
        return draw_triangle(triangleSide)  
    elif (shape == "S" or shape== "s" or shape == 'square' or shape == 'Square'): 
        squareSide = int(input('Square side length: '))
        return draw_square(squareSide)
    else:
        return 'Invalid :('
   
chooseShape = input('What shape shall I draw for you today? ')

shape_choice(chooseShape)
print(chooseShape)

