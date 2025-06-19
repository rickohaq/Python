name = "ricko"
# DECLARED GLOBALY
def print_name():
    # name = "aqsa" 
    def inner_function():
        print(name)
    inner_function()
    # DALAM FUNCTION VAR OUJTER FUNCTION DAPAT DI PANGGIL DALAM INNER FUNCTION
  

# GLOBAL SCOPE
# print(name)


print_name()


