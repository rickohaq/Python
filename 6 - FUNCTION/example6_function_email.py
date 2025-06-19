email = input ("masukan username: ")
domain = input ("masukan domain: ")

def create_email(email,domain):
    """
    function ini untuk membuat email@domain.com
    """
    print(f"email anda adalah {email}@{domain}.com")


create_email(email,domain)

print(create_email.__doc__)
# __doc__ ini mirip help