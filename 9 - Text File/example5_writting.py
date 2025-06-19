# with open("text2.txt","w") as f:
#     add_text = "router bgp 65001\n router-id 1.1.1.1" 
#     f.write(add_text)
  

# print("\n")
# print(f)
# JIKA HANYA OPEN "W" DAN CLOSE MAKA DATA TEXT FILE AKAN TEROVERIDE DENGAN NONE, JADI TEXT FILE KOSONG

# with open("text2.txt", "w") as f:
#     f.write("this is line no 1")
#     f.write("this is line no 2")

# kalau ingin baris 2 ter save gunakan \n dalam f.write pertama
with open("text2.txt", "w") as f:
    f.write("this is line no 1\n")
    f.write("this is line no 2")
