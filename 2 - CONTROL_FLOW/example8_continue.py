my_list_of_devices = ["SPINE1", "SPINE2", "LEAF1", "LEAF2"]

# for device in my_list_of_devices:
#     if device == "LEAF1":
#         continue
#     print (device)

for device in my_list_of_devices:
    if device.startswith("LEAF"):
        continue
    print(device)