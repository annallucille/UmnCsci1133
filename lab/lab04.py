import turtle
import math
import random




def div27(num):
    for i in range(2,8):
        if num % i == 0:
            return True

def mul(a,b):
    sum = a
    for i in range(1,b):
        sum += a
    print(sum)

def expo(x,y):
    product = 1
    for j in range(y):
        product = mul(x,product)
    print(product)
    
def drunkards_walk(max):
    for k in range(1,max):
        angle = random.randint(1,4) * 90
        turtle.setheading(angle)
        turtle.forward(30)
        
def escape(box):
    x = 0
    y = 0
    i=0
    while x in range(-box,box) and y in range(-box,box):
        drunkards_walk(2)
        x = int(turtle.xcor())
        y = int(turtle.ycor())
        i+=1
    print(i)
    turtle.setpos(0,0)
    turtle.write(i, font=("Arial", 20, "normal"))
        

    