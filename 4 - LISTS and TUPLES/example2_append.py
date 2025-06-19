my_ip_address = ["10.0.0.1/24", "20.0.0.1/24","30.0.0.0/24" ,"114.5.5.5","8.8.8.8"]
my_public_ips = []

for ip_address in my_ip_address:
    if "10.0" not in ip_address:
    #     print(ip_address)
        # my_public_ips.insert(0,ip_address) 
        my_public_ips.append(ip_address)
print(f"my public ip address are {my_public_ips}")