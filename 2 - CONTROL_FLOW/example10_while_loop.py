login_name = input("Please create your login name: ")

# Validasi login name harus tepat 8 karakter
while len(login_name) < 8:
    print("FAILED, Login name must be exactly 8 characters!")
    login_name = input("Please create your login name: ")

# Minta password jika login_name valid
password = input("Please enter your password: ")
print("Account created successfully!")
