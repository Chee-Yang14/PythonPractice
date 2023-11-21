import random
from entity import Entity

class Person(Entity):
    def __init__(self,name):
        self.name = name
        self.health = 100
    
    def attack(self,zombie):
        randNum = random.randint(1,20)
        if(randNum>=10):
            zombie.health =0
        else:
            print(f"{self.name} attack {zombie.name} and did {randNum} damage")
            zombie.health -= randNum