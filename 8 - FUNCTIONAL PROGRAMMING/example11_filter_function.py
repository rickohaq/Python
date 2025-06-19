my_num = [1,2,3,4,5,6,7,8,9]

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
genap = filter (even,my_num)
print(genap)
print(list(genap))


# ✅ Why does it only print even numbers?
# Because your even() function is designed to return True only when a number is even (num % 2 == 0). The filter() function includes only items for which the function returns True.

# So, filter(even, my_num) means:

# “Give me only the numbers in my_num where even(number) is True.” 