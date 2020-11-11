class Cat:
    def __init__(self,name,sex,color,breed):
        self.name = name
        self.sex = sex
        self.color = color
        self.breed = breed
        self.fight = False
        self.enegry = 100
    def move(self,distance):
        self.energy = 100
        self.enegry = self.enegry - (distance//5)
        return self.enegry

    def __str__(self):
        return f"Name:{self.name}  : sex:{self.sex} color:{self.color} breed:{self.breed}"


animal = Cat('Simba','boy','yellow','mei-kun')
animal.move(100)
print(animal)

