harga_switch = {"cisco":1000, "arista":900, "nokia": 800, "edgecore":500, "aruba":750}
# print(sorted(harga_switch))

harga_server = {"hpe":2000, "dell":1400, "lenovo":1200, "inspur":999}

harga_infra = {**harga_switch, **harga_server}
print(harga_infra)