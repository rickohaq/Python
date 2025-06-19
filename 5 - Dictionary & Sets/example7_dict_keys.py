device_info = {"Layer":"SPINE",
          "ASN":65001,
          "platform":"ARISTA EOS",
          "version":"4.23.0M",
          "serial_number":"HALFH1I3R318YR"
             }
print(device_info)

print(device_info.keys()) 

print(type(device_info.keys()))

list_of_keys = list(device_info.keys())

print(list_of_keys)
print(type(list_of_keys))