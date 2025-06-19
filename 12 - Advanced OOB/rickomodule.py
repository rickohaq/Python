import random

class CreateEmail:
    _provider = ["google.com", "google.co.id"] # _ Private attribute FUNGSINYA agar attribute tersebut tidak dapat di ubah
    def __init__(self,name):
        self.name = name
    def generate(self):
        suffix = random.choice(self._provider)
        self.email = f"{self.name}@{suffix}"
    def __str__(self):
        return self.email


# ricko = CreateEmail("ricko")
# ricko.generate()
# print(ricko)