
# Inheritance: “A is a B” → Contoh: Anjing is a Hewan

# Composition: “A has a B” → Contoh: Mobil has an Mesin

class Dog:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def sounds(self):
        return "WOOF!"
    
class Bulldog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def breathing (self):
        return "huft"
    def sounds(self):
        return "GUK GUK!"
hachiko = Bulldog("hachiko", 1)
print(hachiko.name)
print(hachiko.age)
print(hachiko.sounds())    # warisan dari Dog
print(hachiko.breathing()) # method dari Bulldog

zeus = Dog("zeus", 2)
print(zeus.name)
print(zeus.age)
print(zeus.sounds())
# print(zeus.breathing) # AttributeError: 'Dog' object has no attribute 'breathing'