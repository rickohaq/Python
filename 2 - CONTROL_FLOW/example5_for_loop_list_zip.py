interface_list = ["gig0/1", "gig0/2", "gig0/3"]
ip_address_list = ["10.0.0.1/24", "20.0.0.1/24","30.0.0.0/24"]

# for interface in interface_list:
#     print (f"interface {interface}\n no shutdown")
# for ip_address in ip_address_list:
#     print(f"ip address {ip_address}")
    
for interface, ip_address in zip(interface_list, ip_address_list):
    print(f"interface {interface}")
    print(f" ip address {ip_address}")
    print(" no shutdown")
    print()