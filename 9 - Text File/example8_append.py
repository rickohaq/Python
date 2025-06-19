with open("new.txt","a") as f:
    add_new_line = "this is new line to be put in"
    f.writelines(add_new_line)
    f.writelines("\nadd another one")