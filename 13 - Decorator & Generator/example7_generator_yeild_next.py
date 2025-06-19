# def square_me (list_of_my_nums):
#     my_list = []
#     for num in list_of_my_nums:
#         my_list.append(num * num)
#     return my_list

# square_list = square_me([1,2,3,4,5,6,7,8,9,10,11,12,13])
# print(square_list)

#cara lebih efektif dengan generator yield (less memory krn tidak simpan list)

def square_me (list_of_my_nums):
    for num in list_of_my_nums:
        yield(num * num)

generator_object = square_me([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(generator_object)

print(next(generator_object))
print(next(generator_object))
print(next(generator_object))

new_generator_object= square_me([1,2,3,4,5,6,7,8,9,10,11,12,13])
type(new_generator_object)
for x in new_generator_object:
    print(x)
# Python automatically handles the next() calls for you — it keeps calling next() until the generator is exhausted.



# Behind the scenes, Python does something like this:
# it = iter(new_generator_object)   # get the iterator (in this case, it's the generator itself)
# while True:
#     try:
#         x = next(it)              # get next value
#         print(x)
#     except StopIteration:
#         break                     # no more items — exit the loop
