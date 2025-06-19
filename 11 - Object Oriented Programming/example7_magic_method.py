class Student:
    def __init__(self, age , course):
        self.age = age
        self.course = course
    def __str__(self):
        return f"I am student, aged {self.age} and I am studying {self.course}"
    
ricko = Student(34, "Network Automation")
print(ricko)
        