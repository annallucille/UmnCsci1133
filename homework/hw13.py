import turtle, random
############################## Problem (A) ###############################
SCALE = 32
class Game:
    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)

        self.active = Block()
        self.occupied = []
        
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        


        #These three lines must always be at the BOTTOM of __init__
        turtle.ontimer(self.gameloop, 300)
        turtle.update()
        turtle.listen()
        turtle.mainloop()
        
    def gameloop(self):
        if self.active.valid(0,-1,self.occupied) == True:
            self.active.move(0,-1)
            turtle.ontimer(self.gameloop, 300)
            turtle.update()
        else:
            for square in self.active.squares:
                self.occupied.append(square)
            self.line_pop()
            self.active = Block()
            self.game_end()
            self.gameloop()
            turtle.update()
        
    def move_left(self):
        if self.active.valid(-1,0,self.occupied) == True:
            self.active.move(-1, 0)
            turtle.update()
        
    def move_right(self):
        if self.active.valid(1,0,self.occupied) == True:
            self.active.move(1, 0)
            turtle.update()
    

    def line_pop(self):
        for y in range(18):
            squares_y = []
            for square in self.occupied:
                if square.turtle.ycor() == y:
                    squares_y.append(square)
            if len(squares_y) == 10:
                for square in squares_y:
                    self.occupied.pop()
                    square.turtle.clear()
                    square.turtle.update()
                    turtle.update()
                    
    def game_end(self):
        for square in self.occupied:
            if square.turtle.ycor() >= 20:
                turtle.bye()
                quit()

                

        
    


class Square():
    def __init__(self, x, y, color):
        self.turtle = turtle.Turtle()
        self.turtle.shape('square')
        self.turtle.shapesize(SCALE/20)
        self.turtle.speed(0)
        self.turtle.fillcolor(color)
        self.turtle.pencolor('gray')
        self.turtle.penup()
        self.turtle.goto(x,y)
    def delete(self):
        self.turtle.clear()
        turtle.update()
        
        
        
        
    
class Block:
    def __init__(self):
        color = random.choice(['pink', 'blue', 'purple', 'cyan'])
        self.shapes = {'Square':[Square(4,22,color),Square(5,22,color),Square(4,23,color),Square(5,23,color)],
                       'L': [Square(3,22,color),Square(4,22,color),Square(5,22,color),Square(5,23,color)],
                       'J':[Square(4,23,color),Square(4,22,color),Square(5,22,color),Square(6,22,color)],
                       'Cross': [Square(4,22,color),Square(5,22,color),Square(6,22,color),Square(5,23,color)],
                       'Zig': [Square(4,21,color),Square(5,21,color),Square(5,22,color),Square(6,22,color)],
                       'Zag': [Square(4,23,color),Square(5,23,color),Square(5,22,color),Square(6,22,color)],
                       'Line': [Square(4,22,color),Square(5,22,color),Square(6,22,color),Square(7,22,color)],
                       'Vert': [Square(5,22,color),Square(5,23,color),Square(5,24,color),Square(5,25,color)]}
        self.squares=self.shapes[random.choice(['Square','J','L','Cross','Zig','Zag','Line','Vert'])]
        print(self.squares)
  
    def move(self, dx, dy):
        for square in self.squares:
            x = square.turtle.xcor() + dx
            y = square.turtle.ycor() + dy
            square.turtle.goto(x,y)
        
    def valid(self,dx,dy,occupied):
        for square in self.squares:
            x = square.turtle.xcor() + dx
            y = square.turtle.ycor() + dy
            if x < 0 or x > 9 or y < 0:
                return False
            for other_square in occupied:
                if x ==  other_square.turtle.xcor() and y == other_square.turtle.ycor():
                    return False
        return True

               


if __name__ == '__main__':
    Game()
