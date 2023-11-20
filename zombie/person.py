from entity import Entity

class Person(Entity):
    def __init__(self,name):
        self.name = name
        self.health = 100
        