username = input ("masukan username: ")
hostname = input ("masukan hostname: ")
platform = input ("masukan platform: ")

plat = platform.lower()

def login_access (username,hostname,plat):
    if plat == "cisco":
        print(f"enable\nconfigure terminal\nshow running-config")
    if plat == "nokia":
        print(f"edit [candidate]\n info flat")
login_access (username,hostname,plat)








# # bisa buat default value plat = cisco

# def login_access (username,hostname,plat="cisco"):
#     if plat == "cisco":
#         print(f"enable\nconfigure terminal")
# login_access (username,hostname)