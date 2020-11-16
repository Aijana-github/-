class Personaji:
    def __init__(self,name,position,age,race,weight,height):
        self.name = name
        self.position = position
        self.age = age
        self.race = race
        self.weight = weight
        self.height = height
        self.strong = True





    def description(self):
        print(self.name,self.position,self.age,self.race,self.strong,self.move,self.weight,self.height)

class Panda(Personaji):
    def __init__(self,name,position,age,race,weight,height):
        self.position = position
        self.weight = weight
        self.height = height
        self.strong = "strong"


        super().__init__(name,position,age,race,weight,height)

    def description(self):
        print(self.name,self.position,self.age,self.race,self.strong,self.move,self.weight,self.height,self.strong,self.move)
    def move(self,new_position):
        self.position = new_position

class LaraKroft():
    def __init__(self,name,position,age,race,weight,height):
        self.name = name
        self.position = position
        self.age = age
        self.race = race
        self.weight = weight
        self.height = height
        self.strong = "strong"
        self.property = "foxy"

        super().__init__(name,position,age,race,weight,height)

    def description(self):
        print(self.name,self.position,self.age,self.race,self.weight,self.heights,self.strong,self.property)



panda = Panda("Po",17,25,"asian",500,3)
panda.description()
panda.move(13)
laraKroft = LaraKroft("Jolie",11,25,"asian",55,2)
laraKroft.strong(50)
laraKroft.description()














