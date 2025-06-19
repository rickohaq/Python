device_info = {"Layer":"SPINE",
          "ASN":65001,
          "platform":"ARISTA EOS",
          "version":"4.23.0M",
          "serial_number":"HALFH1I3R318YR"
             }
print(device_info)

print(device_info.values()) 

print(type(device_info.values()))

list_of_values = list(device_info.values())

print(list_of_values)
print(type(list_of_values))