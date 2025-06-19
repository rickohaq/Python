# def calcu(my_list):
#     total = 0
#     for angka in my_list:
#         total = total + angka
#     print(total)

# calcu([1,2,3,5])

def better_calcu(*args):
    total = 0
    for angka in args:
        total = total + angka
    print(total)

better_calcu(1,2,3,5)