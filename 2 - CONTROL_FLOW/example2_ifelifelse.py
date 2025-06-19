vendor = input("Enter the vendor you wish to automate: ").lower()

if vendor == "cisco":
    print("You have selected Cisco")
elif vendor == "juniper":
    print("You have selected Juniper")
elif vendor == "arista":
    print("You have selected Arista")
elif vendor == "nokia":
    print("You have selected Nokia")
elif vendor == "aruba":
    print("You have selected Aruba")
else:
    print("Unrecognised vendor")