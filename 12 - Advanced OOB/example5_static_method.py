
# | Method Type     | Decorator       | First Argument | Can Access Instance (`self`) | Can Access Class (`cls`) |
# | --------------- | --------------- | -------------- | ---------------------------- | ------------------------ |
# | Instance Method | *(none)*        | `self`         | ✅ Yes                        | ✅ via `self.__class__`   |
# | Class Method    | `@classmethod`  | `cls`          | ❌ No                         | ✅ Yes                    |
# | Static Method   | `@staticmethod` | None           | ❌ No                         | ❌ No                     |

skill = ["networking", "linux", "python", "ansible"]

import random

class NewTrainer:
    def __init__(self,skill):
        self._skill = skill
    
    @property
    def skill(self):
        return self._skill
    
    @staticmethod
    def random_skill():
        return NewTrainer(random.choice(skill))

new_cbtn_person = NewTrainer.random_skill()

print(new_cbtn_person._skill)
