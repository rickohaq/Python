my_list_of_protocol = ["RIP","OSPF","EIGRP","ISIS"]

if "BGP" not in my_list_of_protocol:
    print("no path vector protocol are present")
else:
    print("path vector detected")