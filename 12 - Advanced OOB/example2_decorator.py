class Stundent:
    def __init__(self, name, studentnum):
        self._name = name
        self._studentnum = studentnum
    def name(self):
        return self._name
    def studentnum(self):
        return self._studentnum
 

ricko = Stundent("ricko", 111080273)
print(ricko._name)
print(ricko._studentnum)

print(ricko.name)
print(ricko.studentnum)

print(ricko.name())
print(ricko.studentnum())


