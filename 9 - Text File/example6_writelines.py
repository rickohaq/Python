
with open("text2.txt", "w") as f:
    my_list = ["router bgp 65001\n", "router-id 1.1.1.1\n","maximum-paths 4 ecmp 64\n"]
    f.writelines(my_list)