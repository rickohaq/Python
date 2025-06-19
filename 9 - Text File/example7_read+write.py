# with open ("original.txt", "r") as source, open("new.txt","w") as destination:
#     text_data = source.readlines()
#     for line in text_data:
#         destination.writelines(line)

with open ("original.txt", "r") as source, open("new.txt","w") as destination:
    text_data = source.readlines()
    for line in text_data:
        destination.writelines(line.capitalize())

