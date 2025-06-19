file = open  ("text1.txt")
print(dir(file))

print(file)
file.close()

# jika kita tidak close bisa jadi bug.. change file harus di close agar tersave