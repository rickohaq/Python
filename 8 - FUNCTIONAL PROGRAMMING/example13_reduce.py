from functools import reduce

# my_num = [1,2,3,4,5]

# def adder(x,y):
#     result = x + y 
#     return result

# hasil = reduce(adder,my_num)
# # print(hasil)

# reduce akan ambil variable dalam list sesuai dengan list 2
# You're trying to use a reduce() function with adder(x, y, z), but reduce() only works with functions that take exactly two arguments (a running accumulator and the next item in the list).

my_num2 = [11,2,3,42,5,11,30,55]
hasil2 = reduce(lambda x,y : x if x > y else y, my_num2)

print(hasil2)