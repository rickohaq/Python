# Composition (komposisi) adalah hubungan antar objek di mana:

# Satu class mengandung (memiliki) objek dari class lain.

# 🟡 Beda dengan Inheritance:
# Inheritance: “A is a B” → Contoh: Anjing is a Hewan

# Composition: “A has a B” → Contoh: Mobil has an Mesin
# Dan class Person punya (has a) objek Payment.


class Payment:
    def __init__(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
    def salary(self):
        return(self.wage * 52) + self.bonus

class Person:
    def __init__(self, name, age, wage , bonus):
        self.name = name
        self.age = age
        self.obj_payment = Payment(wage,bonus)  # komposisi di sini!

    def yearly_wage(self):
        return self.obj_payment.salary()  # panggil method dari Payment

    
ricko = Person("ricko", 34, 3400,1000)
print(ricko.yearly_wage())