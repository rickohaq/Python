my_name = ["ricko","diah","mecca", "aqsa"]
def normalize_data (word):
    return word.upper()
print(normalize_data("ricko"))

my_fixed_name = list (map(normalize_data,my_name))
print(my_fixed_name)

