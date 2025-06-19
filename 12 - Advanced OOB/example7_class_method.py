class Human:
    _needs = ["air", "water", "food"]  # ← class variable (shared by all)

    def __init__(self, name):
        self._name = name  # ← instance variable (unique to each object)

    @classmethod
    def needs(cls):
        return cls._needs # INI AKAN ambil class variable _need dalam class Humas diatas
    # cls points to the class Human, not a particular object like john
    # cls._needs accesses the class-level variable (shared by all humans)
    # This is how classmethods work: they operate on the class, not on one object.

john = Human("john")
# Now john is an object (instance) of the Human class. Inside the constructor __init__,
# self._name = name sets a variable just for john. If you made another human like jane, she’d have a different self._name.
# So:
# self is the object itself
# self._name is instance data (specific to each object)

print(john._needs)
john._needs = ["pizza", "ice cream","coffe"]
print(john._needs)
print(john.needs())