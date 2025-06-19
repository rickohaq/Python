
class Stundent:
    def __init__(self, name, studentnum):
        self._name = name
        self._studentnum = studentnum
    @property # getter ini untuk agar tidak perlu panggil ()
    def name(self):
        return self._name
    @property
    def studentnum(self):
        return self._studentnum
 

ricko = Stundent("ricko", 111080273)

print(ricko.name)
print(ricko.studentnum)

