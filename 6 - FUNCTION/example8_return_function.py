# email = input ("masukan username: ")
# domain = input ("masukan domain: ")

def create_email(username,provider):
    """
    function ini untuk membuat email@datacomm.co.id
    """
    email_addr = f"{username}@{provider}.co.id"
    return email_addr
# ini untuk simpan hasil function dalam var email_addr

nama_karyawan_baru = ["ahmad","isna","habibi"]
email_baru_list= []

for karyawan in nama_karyawan_baru:
    new_email= create_email(karyawan, "datacomm")
    (email_baru_list.append(new_email))

print(email_baru_list)
