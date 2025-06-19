# my_list= ["ricko","diah", "mecca", "aqsa"]
# print(my_list.__len__())

class Family:
    members= ["ricko","diah", "mecca", "aqsa"]
    def __len__(self): #__xx__ ini magic method
        return len(self.members)

my_family = Family()
# print(dir(my_family))
# print(my_family)

print(len(my_family))

