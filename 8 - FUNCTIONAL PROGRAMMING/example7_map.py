my_list = [1, 2, 3, 6, 7, 11, 13]
def kuadrat(num):
    return num **2

new_list = map (kuadrat,my_list)
print (new_list)

print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))

print(list(new_list))
#melihat sisa list dari new_list