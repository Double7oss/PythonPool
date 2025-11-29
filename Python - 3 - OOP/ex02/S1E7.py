from S1E9 import Character


class Baratheon(Character):
    """ Representing the baratheon family """
    def __init__(self, first_name, is_alive = True,
                family_name="Baratheon", eyes = 'brown', hairs = 'dark'):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def die(self):
        self.is_alive = False
    
    def __str__(self):
        return f"Vector: {self.family_name} , {self.eyes}, {self.hairs}"
    
    def __repr__(self):
        return f"Vector: {self.family_name}, {self.eyes}, {self.hairs}"


class Lannister(Character):
    def __init__(self, first_name, is_alive= True, family_name='Lannister', eyes = 'blue', hairs='light'):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def die(slef):
        slef.is_alive = True
    
    def __str__(self):
        return f"Vector: {self.family_name}, {self.eyes}, {self.hairs}"
    
    def __repr__(self):
        return f"Vector: {self.family_name}, {self.eyes}, {self.hairs}"
    
    @classmethod
    def create_lannister(cls,first_name, is_alive):
        return cls(first_name, is_alive)