class Personaji:
    def __init__(self,name,position,age,race,weight,height):
        self.name = name
        self.position = position
        self.age = age
        self.race = race
        self.weight = weight
        self.height = height
        self.strong = True
        self.move = True



    def description(self):
        print(self.name,self.position,self.age,self.race,self.strong,self.move,self.weight,self.height)

class Panda(Personaji):
    def __init__(self,name,position,age,race,weight,height):
        self.position = position
        self.weight = weight
        self.height = height
        self.strong = True
        self.move = True

        super().__init__(name,position,age,race,weight,height)

    def description(self):
        print(self.name,self.position,self.age,self.race,self.strong,self.move,self.weight,self.height,self.strong,self.move)


panda = Panda("Po",'china',25,'asian',500,3)
panda.description()














