class Planet:
    def __init__(self,name,position):
        self.name = name
        self.form = 'shape'
        self.position = position
        self.temp = 0
        self.size = 0

    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size)

class Mercury(Planet):
    def __init__(self,position,name='Mercury'):
        super().__init__(name,position)
        self.temp = 120
        self.size = 'small'

class Jupiter(Planet):
    def __init__(self,position,name='Jupiter'):
        super().__init__(name,position)
        self.temp = 999
        self.size = 'big'
        self.brilliant_rain = True

    def discription(self):
        print(self.name,self.form,self.position,self.temp,self.brilliant_rain)

class Saturn(Planet):
    def __init__(self,position,name='Saturn'):
        super().__init__(name,position)
        self.temp = -100
        self.size = 'middle'
        self.rings = True
        self.count_rings = 7

    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size,self.count_rings)



mercury = Mercury('Solar system')
mercury.description()
jup = Jupiter('Solar system')
jup.description()
saturn = Saturn('Solar system')
saturn.description()


