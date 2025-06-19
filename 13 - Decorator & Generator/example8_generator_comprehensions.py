my_list_comp = [num*num for num in range (1,99999)]

my_gen_comp = (num*num for num in range (1,99999))
# print(my_list_comp)
print(my_gen_comp)

for x in my_gen_comp:
    print(x)

import sys

print(sys.getsizeof(my_list_comp))
print(sys.getsizeof(my_gen_comp))

#lebih irit memory pakai generator 