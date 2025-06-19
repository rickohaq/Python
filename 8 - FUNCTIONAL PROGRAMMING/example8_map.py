my_list = [1, 2, 3, 6, 7, 11, 13]

# def kuadrat(num):
#     return num **2

# my_new_kuadrat_list = map (kuadrat, my_list)

# print(list(my_new_kuadrat_list))


my_list_use_lambda = list (map(lambda x: x**2 , my_list))

print(my_list_use_lambda)

# JIKA ingin looping list dalam function/lambda map lah cara nya
# use_map = list (map(lambda x : x +1 , my_list))

for num in my_list_use_lambda:
    print(num)