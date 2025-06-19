# | Feature                  | Instance Method | Class Method | Static Method |
# | ------------------------ | --------------- | ------------ | ------------- |
# | Has access to `self`     | ✅ Yes           | ❌ No         | ❌ No          |
# | Has access to `cls`      | ❌ No            | ✅ Yes        | ❌ No          |
# | Can access instance data | ✅ Yes           | ❌ No         | ❌ No          |
# | Can access class data    | ✅ (via self)    | ✅ Yes        | ❌ No          |


class Example:
    class_var = "I am a class variable"

    def __init__(self, name):
        self.name = name  # instance variable

    def instance_method(self):
        print("Instance method")
        print("Can access instance (self):", self.name)
        print("Can access class (via self):", self.class_var)

    @classmethod
    def class_method(cls):
        print("Class method")
        print("Can access class (cls):", cls.class_var)
        # print(cls.name)  # ❌ Error, no access to instance

    @staticmethod
    def static_method():
        print("Static method")
        # Can't do this:
        # print(self.name)  ❌ self not defined
        # print(cls.class_var) ❌ cls not defined

test = Example.static_method()