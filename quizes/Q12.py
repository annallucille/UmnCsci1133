
##################### Q(3) #####################

class Item:
    def __init__(self,size):
        self.size = size
    def __repr__(self):
        return 'Item size: ' + str(self.size)
    def __lt__(self,other):
        if self.size<other.size:
            return True
        else:
            return False

class NamedItem:
    def __init__(self,size,name):
        Item.__init__(self, size)
        self.name = name
    def __repr__(self):
        return Item.__repr__(self) + ' Item name: ' + self.name
    def __lt__(self,other):
        if self.size == other.size:
            if self.name < other.name:
                return True
            else:
                return False
        else: 
            return Item.__lt__(self,other)
        
        
#################### Q(4) #####################

class Warehouse: 
    def __init__(self,addy, ls=[] ):
        self.addy=addy
        self.lst=ls
    def normilize(self):
        for i in range(len(self.lst)-1):
            if NamedItem.__lt__(self.lst[i],self.lst[i+1]) == False:
                self.lst.append(self.lst[i])
                self.lst[i]=self.lst[i+1]
                self.lst.pop(i+1)
            else: 
                Warehouse.normilize(self)
        return self.lst
    def add_item(self,item):
        self.lst.append(item)
    def __add__(self,other):
        self.lst = self.lst + other.lst
        return Warehouse.normilize(self.lst)
    def __repr__(self):
        prt_lst =[]
        for item in self.lst:
            cls = item.__class__
            if cls == Item:
                prt_lst.append(Item.__repr__(item))
            else:
                prt_lst.append(NamedItem.__repr__(item))
        return str(prt_lst)
            
