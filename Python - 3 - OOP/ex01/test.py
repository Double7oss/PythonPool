from S1E7 import Baratheon, Lannister

obj = Baratheon("Houssam")
print(obj.__dict__)
print(obj.__str__)
print(obj.__repr__)
print(obj.is_alive)
obj.die()
print(obj.is_alive)
print(obj.__doc__)

print("---")

Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)

print("---")

Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")