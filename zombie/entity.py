class Entity:
    def __init__(self,name):
        self.name = name
        self.health = 10
        
    def __str__(self):
         return f"name: {self.name}\nhealth: {self.health}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name = name
     
    @property 
    def health(self):
         return self._health
    
    @health.setter
    def health(self, health):
        self._health = health

