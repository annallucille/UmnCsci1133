
####################### Problem (A) ##########################

class Crew: 
    def __init__(self, name):
        self.name = name
        self.status = 'Active'
        self.location = 'Sleep Pods'
    def __repr__(self):
        return '<'+self.name+'> : <'+self.status+'>, at <'+self.location+'>'
    ###################### Problem (C) #####################
    def move(self,location):
        locations = ["Bridge", "Medbay", "Engine", "Lasers", "Sleep Pods"]
        if location in locations:
            self.location = location 
        else: 
            print('Not a valid location.') 
    def repair(self, ship):
        print('<'+self.name+'> doesn\'t know how to do that.')
    def first_aid(self, ship):
        print('<'+self.name+'> doesn\'t know how to do that.')
    def fire_lasers(self, ship, target_ship, target_location):
        print('<'+self.name+'> doesn\'t know how to do that.')

    
    
####################### Problem (B) ##########################

class Starship: 
    def __init__(self, name, crew_list):
        self.name = name
        self.crew_list = crew_list
        self.damaged = {'Bridge':False, 'Medbay':False, 'Engine':False,
            'Lasers':False, 'Sleep Pods':False}
        

######################### Problem (D) ########################

class Engineer(Crew): 
    # def __init__(self):
    #     Crew.__init__(self)
    def repair(self, ship: Starship):   
        if ship.damaged[ self.location] == True:
            ship.damaged[self.location] =False 
            print('<'+self.name+'> fixed the damage to <'+self.location+'>.')
        elif ship.damaged[self.location] == False:
            print('<'+self.location+'> isn\'t damaged.')
            
class Captian(Crew):
    def fire_lasers(self, ship: Starship, target_ship: Starship, target_location):
        