import turtle

##################################### Warm Up #######################################

class Rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return 0
        else:
	        return str(self.numerator) + '/' + str(self.denominator)
     
     

##################################### Stretch #######################################

class Vec2:
    def __init__(self,x=0,y=0):
        self.v1=x
        self.v2=y
    def __str__(self):
        return '<' + str("{:.2f}".format(self.v1))+ ',' + str("{:.2f}".format(self.v2)) + '>'
    def get_values(self):
        return [float(self.v1),float(self.v2)]
    def set_values(self,lst):
        self.v1=lst[0]
        self.v2=lst[1]
    def  __add__(self,other):
        x = self.v1 + other.v1
        y = self.v2 + other.v2
        return Vec2(x,y)
    def  __mul__(self, scalar):
        x = self.v1 * scalar
        y= self.v2 * scalar
        return Vec2(x,y)
    
    
    

##################################### Work Out #######################################

class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.pos = pos 
        self.vel = vel 
        self.t = turtle.Turtle()	
        self.t.shape("circle")
        self.t.speed(0)
        self.t.penup()
        self.move()  
        self.t.pendown()
    def __str__(self):
        return 'mass:' + str(self.mass) + ', pos:' + str(self.pos) + ', vel:' +str(self.vel)
    def move(self):
        Vec2.__init__(self)
        turtle.setpos(self.v1,self.v2)
    def accelerate(self, a, t):
        Vec2.__init__(self)
        self.pos.v1 = self.pos.v1 + self.vel.v1*t+.5*a.v1*(t**2)
        self.pos.v2 = self.pos.v2 + self.vel.v2*t+.5*a.v2*(t**2)
        self.vel.v1 = self.vel.v1+a.v1*t
        self.vel.v2 = self.vel.v2+a.v2*t

if __name__ == '__main__':
    p1 = Particle(50,Vec2(-200,-50),Vec2(30,30))
    p2 = Particle(20,Vec2(100,50),Vec2(-20,0))
    print(p2) #should output mass:20, pos:<100, 50>, vel:<-20, 0>
    p2.accelerate(Vec2(0,-10),2)
    print(p2) #should output mass:20, pos:<60.0, 30.0>, vel:<-20, -20>
    p2.accelerate(Vec2(20,20),3)
    print(p2) #should output mass:20, pos:<90.0, 60.0>, vel:<40, 40>
    for i in range(100):
        p1.accelerate(Vec2(0,-10),0.1)
        p2.accelerate(Vec2(0,-10),0.1)
    print(p1) #should output mass:50, pos:<100.0, -250.0>, vel:<30.0, -70.0>
    print(p2) #should output mass:20, pos:<490.0, -40.0>, vel:<40.0, -60.0>
