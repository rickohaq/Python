class Drummer():
    member_type = "Percussionist" 
    def __init__(self, style, lead_hand, brand): #ini namanya instance attribute first attribute usahakan gunakan self.. namun tidak wajib bisa apapun
        self.style = style
        self.lead_hand = lead_hand
        self.brand = brand

# ricko = Drummer() 
# akan muncul error
# TypeError: GuitaDrummerrist.__init__() missing 3 required positional arguments: 'style', 'lead_hand', and 'brand'

ricko = Drummer ("rock", "right-handed", "Yamaha")

print(ricko.brand)
print(ricko.member_type)
print(ricko.style)
print("\n")
aqsa = Drummer("jazz", "left-handed", "Gibson")
print(aqsa.brand)
print(aqsa.member_type)
print(aqsa.style)