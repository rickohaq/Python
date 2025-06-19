# nested loop adalah loop dalam loop
my_list_of_devices = ["SPINE1", "SPINE2", "LEAF1", "LEAF2"]
interface_list = ["gig0/1", "gig0/2", "gig0/3"]
ip_address_list = ["10.0.0.1/24", "20.0.0.1/24","30.0.0.0/24"]

for devices in my_list_of_devices:
    print (f"this is configuration for {devices}")
    for interface, ip_address in zip(interface_list, ip_address_list):
        print(f"interface {interface}\nDescription this is interface {interface} on {devices}")
        # print(f" ip address {ip_address}")
        print("MTU 9214")
        print("no shutdown")
        print()