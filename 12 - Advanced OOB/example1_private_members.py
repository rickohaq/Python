from rickomodule import CreateEmail

my_email = CreateEmail("diah.natasyah")
my_email._provider = ["dcloud.co.id", "dcloud.id"] #kita tetap dapat overide dengan _ kembali, tetap bisa dipaksa
my_email.generate()
print(my_email)