import ipaddress
network = ipaddress.ip_network("10.0.0.0/28")

# for host in network.hosts():
#     print(host)

print(network.netmask)
print(network.hostmask)

my_ip = ipaddress.ip_address("10.0.0.1")

address1 = ipaddress.ip_network("10.0.0.1/30", strict=False)
address2 = ipaddress.ip_network("10.0.0.5/30", strict=False)

print(address1)
print(address2)

if address1 == address2:
    print("same subnet")
else:
    print ("different subnet")