my_new_list_of_family = ["nenek", "ichira" , "alfarisi"]

class Family:
    members= ["ricko","diah", "mecca", "aqsa"]
    def __len__(self): #__xx__ ini magic method
        return len(self.members)
    def __contains__(self, friend):
        return self.members
    
my_family= Family()

if "ricko" in my_family:
    print('Ricko in the list of my family')
else:
    print("ricko not in list of my family")
    
