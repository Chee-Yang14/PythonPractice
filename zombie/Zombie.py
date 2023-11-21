import random
from entity import Entity

class Zombie(Entity):
    pass
        
    def attack(self, person):
         randNum = random.randint(1,10)
         if(randNum>=person.health):
            person.health =0
         else:
            print(f"{self.name} attack {person.name} and did {randNum} damage")
            person.health -= randNum