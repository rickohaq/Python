my_list = [1,2,3,[3,2,5,1],7,45,22]
# print(my_list)

for num in my_list:
    # print(num)
    if isinstance(num,list):
        for n in num:
            if n == 5:
                print(n)