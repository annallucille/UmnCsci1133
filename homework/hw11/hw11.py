import random

######################## Problem (A) ###########################

class Boat: 
    def __init__(self, name ='', speed =3):
        self.boat_name = name
        self.top_speed = speed
        self.current_progress = 0
    def __str__(self):
        return self.boat_name + ': ' + str(self.current_progress)
    def set_top_speed(self,speed):
        self.top_speed = speed
    def set_boat_name(self, name):
        self.boat_name = name
    def set_current_progress(self,progress):
        self.current_progress = progress
    def get_boat_name(self):
        return self.boat_name
    def get_top_speed(self):
        return self.top_speed
    def get_current_progress(self):
        return self.current_progress
    def move(self):
        x = random.randint(0, self.top_speed)
        self.current_progress+=x
        return x
    
if __name__ == '__main__':
    my_boat = Boat("The Fire Ball", 12)
    other_boat = Boat("The Leaf", 100)
    print(type(my_boat)) #<class '__main__.Boat'>
    print(str(my_boat)) #The Fire Ball: 0
    print(my_boat.get_boat_name()) #The Fire Ball
    print(my_boat.get_top_speed()) #12
    print(my_boat.get_current_progress()) #0
    print(my_boat.move()) #Some number between 0 and 12
    print(my_boat.get_current_progress()) #Same num as prev line
    print(my_boat.move()) #Another number between 0 and 12
    print(my_boat.get_current_progress()) #Sum of prev 2 lines
    my_boat.set_top_speed(100)
    my_boat.set_boat_name("The Sam")
    my_boat.set_current_progress(1000)
    print(my_boat) #The Sam: 1000
    print(my_boat.get_current_progress()) #1000
    for i in range(9980):
        my_boat.move()
    print(my_boat.get_current_progress()) #Should be about 500000

    

######################## Problem (B) ###########################

class BoatRace:
    def __init__(self, csv):
        file = open(csv)
        lines = []
        self.racers =[]
        i = -1
        for line in file:
            lines.append(line.split(','))
            i+=1
            if i >= 3:
                self.racers.append(Boat(lines[i][0],int(lines[i][1])))
        self.race_name = lines[0][1].translate({ord('\n'): None})
        self.race_id = int(lines[1][1])
        self.distance = int(lines[2][1])
        self.result = []
    def get_race_name(self):
        return self.race_name
    def get_race_id(self):
        return self.race_id
    def get_distance(self):
        return self.distance
    def get_racers(self):
        return self.racers
    ######################## Problem (C) ###########################
    def add_racer(self, racer):
        Boat.__init__(self)
        self.racers.append(racer)
    def print_racers(self):
        for racer in self.racers:
            print(Boat.__str__(racer))
    def count(self):
        return len(self.racers)
    def race(self):
        if self.result==[]:
            for racer in self.racers:
                racer.move()
                if racer.current_progress >= self.distance:
                    self.result.append(racer)
                    self.print_racers()
            self.print_racers()
            self.race()
            return self.result

        

        
            
            


if __name__ == '__main__':
    the_race = BoatRace('/Users/annallucille/umnCsci1133/homework/hw11/the_big_one.csv')
    print(the_race.get_race_name()) #The Big One 
    print(the_race.get_race_id()) #11
    print(type(the_race.race_id)) #<class 'int'>
    print(the_race.get_distance()) #120
    print(type(the_race.distance)) #<class 'int'>
    print(the_race.get_racers()) #[<__main__.Boat object at 0x03A2E4C0>, <__main__.Boat object at 0x03A2E4F0>]

if __name__ == '__main__':
    the_race = BoatRace('/Users/annallucille/umnCsci1133/homework/hw11/the_big_one.csv')
    the_race.add_racer(Boat("Late", 2))
    the_race.print_racers() #The Fire Ball: 0
                            #The Leaf: 0
    result = the_race.race() #The Fire Ball: 5
                             #The Leaf: 39
                             #Late: 2
                             #The Fire Ball: 17
                             #The Leaf: 56
                             #Late: 4
                             #The Fire Ball: 19
                             #The Leaf: 145
                             #Late: 4
    print(the_race.race())
    print(result) #[<__main__.Boat object at 0x03A2E4F0>]
    print(result[0].get_boat_name()) #The Leaf
    print(result[0].get_current_progress()) #145



