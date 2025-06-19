# ini adalah print function dengan **kwargs (keyword arguments)

# def print_function(**kwargs):
#     for kata in kwargs:
#         print (f" ini adalah kata {kata} dalam function ")
    
# print_function(nama="ricko", jabatan="network manager", status="permanent")


def print_function(**kwargs):
    for k,v in kwargs.items():
        print(f"ini adalah key {k} dengan value {v}")

print_function(nama="ricko", jabatan="network manager", status="permanent")
