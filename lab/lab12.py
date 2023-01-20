

############################# Warm Up #############################

######### Problem (1) ##########
class Building:
    '''
    Purpose: Represents a public building in St. Paul
    Instance variables:
        self.name: string - the building's name
        self.lat: float - the latitude of the building's location
        self.long: float - the longitude of the building's location
        self.open: float - the building's opening time
        self.close: float - the building's closing time
        self.meeting: boolean - whether building has a meeting room
        self.fields: int - # of softball fields attached to building
    Methods:
        __init__(self, line): Takes in a line from a CSV file 
            representing a building and splits it up to get the data 
            required for each instance variable
        __str__(self): Returns the string representation of this        
            object.  The name of the building is used for this.
        distance(self, other): Takes in two Building objects 
            (self, other) and returns the approximate distance 
            between the two in miles
    '''
    def __init__(self, line):
        data = line.split(',')
        self.name = data[1]
        self.lat = float(data[2])
        self.long = float(data[3])
        self.open = float(data[4])
        self.close = float(data[5])
        self.meeting = (data[6] == 'Yes')
        self.fields = int(data[7])
    def __str__(self):
        return f'{self.name}'
    def distance(self, other):
        dx = (self.long-other.long) * 48.91
        dy  = (self.lat-other.lat) * 69.17
        return (dx**2 + dy**2)**.5
        



########## Problem (2) ############

class Firehouse:
    def __init__(self,line):
        Building.__init__(self,line)
    def is_open(self, time, day):
        return False
    
class Library:
    def __init__(self,line):
        Building.__init__(self,line)
        self.events = []
    def is_open(self, time, day):
        if time >+ self.open and time<+ self.close:
            if day not in self.events:
                return True
            else: 
                return False
        else:
            return False

class Rec:
    def __init__(self,line):
        Building.__init__(self,line)
    def is_open(self, time, day):
        if time >+ self.open and time<+ self.close:
            if day != 'Su':
                return True
            else: 
                return False
        else:
            return False   
    
######### Problem (3) ##########
if __name__ == '__main__':
    with open('/Users/annallucille/umnCsci1133/lab/buildings.csv') as fp:
        lines = fp.readlines()
        station19 = Building(lines[6])
        rondo = Building(lines[11])
        hazel = Building(lines[25])
        print(station19.distance(rondo)) #Should be about 4.3 miles
        print(hazel.distance(station19)) #Should be about 8.9 miles
        library = Library(lines[4]) 
        print(library.is_open(5,'Sat'))
        rec = Rec(lines[8])
        print(rec.is_open(5,'Sat'))
        print(rec.is_open(8,'Su'))
        print(rec.is_open(-1,'Su'))
        firehouse = Firehouse(lines[6])
        print(firehouse.is_open(8,'Sat'))
        
###################### Stretch #####################
class City:
    def __init__(self, name, filename):
        file = open(filename)
        lines = file.readlines()
        self.name = name 
        self.public =[]
        self.meeting = []
        for line in lines[1:]:
            list = line.split(',')
            nm = [*list[1]]
            if nm[1] == 'F':
                self.public.append(Firehouse.__init__(self, line))
            if nm[1] == 'L':
                self.public.append(Library.__init__(self, line))
            if nm[1] == 'R':
                self.public.append(Rec.__init__(self,line))
    ###################### Work Out ##########################
    ########## Problem (1) ###########
    def study_spot(self, time, day):
        for building in self.public:
            if building.is_open(time, day):
                self.meeting.append([building,time,day])
        return self.meeting
    def fire(self, building):
        dist = 500
        for obj in self.public:
            if isinstance(obj, Firehouse):
                nwdist = building.distance(obj)
                if nwdist <= dist:
                    dist = nwdist
        return dist
                
                
                
            