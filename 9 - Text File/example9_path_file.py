with open ("dir1/dir2/dir3/nestedfile.txt","a") as f:
    nambah_kata = "\nthis is new line to be added in nestedfile"
    f.writelines(nambah_kata)

with open ("../../PYTHON/vxlan.txt","a") as f:
    nambah_kata = "\nthis is new line to be added in vxlan"
    f.writelines(nambah_kata)

with open ("../../PYTHON/vxlan.txt","r") as f:
    output = f.read()
    print(output)