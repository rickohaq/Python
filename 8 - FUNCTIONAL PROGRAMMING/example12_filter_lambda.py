my_interfaces = ["gig0/1", "gig0/2", "gig0/3" , "portchannel1","loopback0"]

my_portchannel_iface = list(filter(lambda x:x.startswith("portch"), my_interfaces))
print(my_portchannel_iface)