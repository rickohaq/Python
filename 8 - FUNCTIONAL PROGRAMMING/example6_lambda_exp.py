# def over_under(x):
#     if x < 10:
#         print("nilai kurang dari 10")
#     elif x>10:
#         print("nilai lebih dari 10")

# over_under(11)

x = 11
hasil = lambda x: "nilai kurang dari 10" if x < 10 else "nilai lebih dari atau sama dengan 10"
print(hasil(x))
# Since lambda only supports a single expression, use Python's conditional expression (ternary  operator):
