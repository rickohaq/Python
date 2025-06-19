# my_number_of_path =[1,1,1,1,2,1,2,1,1,4,3]
my_number_of_path =[1,1,1,1,1,1,1,1,1]

my_multipath_list = []
for paths in my_number_of_path:
    if paths > 1:
        my_multipath_list.append(paths)

# print(my_multipath_list)
# jika my_multipath_list tidak empty
if my_multipath_list:
    print(my_multipath_list)
else: 
    print("there is no multipath value")
