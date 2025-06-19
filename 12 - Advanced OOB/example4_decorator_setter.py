class Student:
    def __init__(self, name, studentnum):
        self._name = name
        self._studentnum = studentnum
    @property # getter ini untuk agar tidak perlu panggil ()
    def name(self):
        return self._name
    @property
    def studentnum(self):
        return self._studentnum
    
    @name.setter
    def name (self,name):
        if len(name) < 2:
            raise ValueError("Name must be at least 2 character or more!")
        self._name= name

    @studentnum.setter
    def studentnum(self,studentnum):
        if not isinstance(studentnum,int):
            raise ValueError ("student number must be INTEGER")
        self._studentnum = studentnum
 

ricko = Student("ricko", 11111)
ricko.name= "Rroro"
ricko.studentnum = "R"
print(ricko.name)
print(ricko.studentnum)

