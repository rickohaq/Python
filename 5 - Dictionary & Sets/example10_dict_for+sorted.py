device_info = {"Layer":"SPINE",
          "ASN":65001,
          "platform":"ARISTA EOS",
          "version":"4.23.0M",
          "serial_number":"HALFH1I3R318YR"
             }
for kunci in device_info.keys():
    print(f" this device_info has a key called {kunci}")
print("\n")

for isi in device_info.values():
    print(f" this device_info has a values called {isi}")
print("\n")

for itemms in device_info.items():
    print(itemms)

for kunci_item, value_item in device_info.items():
    print(f" this device_info has a key called {kunci_item}")
    print(f" this device_info has a key called {value_item}")

# untuk print sesuai sort alfabeth

for keys in sorted(device_info.keys()):
    print(keys)

for item in sorted(device_info.items()):
    print(item)