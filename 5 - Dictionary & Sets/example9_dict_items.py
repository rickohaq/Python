device_info = {"Layer":"SPINE",
          "ASN":65001,
          "platform":"ARISTA EOS",
          "version":"4.23.0M",
          "serial_number":"HALFH1I3R318YR"
             }
print(device_info)

print(device_info.items()) 

print(type(device_info.items()))

list_of_items = list(device_info.items())

print(list_of_items)
print(type(list_of_items[0]))