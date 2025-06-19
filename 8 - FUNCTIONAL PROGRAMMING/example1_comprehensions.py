interface_list = ["GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3","Loopback0", "Loopback1"]

# gig_list = []

# for interface in interface_list:
#     if interface.startswith("Gig"):
#         gig_list.append(interface)
# print(gig_list)

gig_list = [interface for interface in interface_list if interface.startswith("Gig")]
print(gig_list)

# cara baca nya dari for
# jika interface dalam interface_list dan hanya jika interface tersebut berawalan gig_list
# maka put value nya dalam interface

uppergig_list = [interface.upper() for interface in interface_list if interface.startswith("Gig")]
print(uppergig_list)

tengig_list = ["10G" for interface in interface_list if interface.startswith("Gig")]
print(tengig_list)

