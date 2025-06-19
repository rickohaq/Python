# with open("text1.txt", "r") as f:
#     # r adalah read only
#     output = f.read()
#     print(output)

# print(output)

# with open("text1.txt", "r") as f:
#     # r adalah read only
#     partial_output = f.read(4)
#     print(partial_output)
    
# with open("text1.txt", "r") as f:
#     # r adalah read only
#     line1_output = f.readline()
#     line2_output = f.readline()
#     print(line1_output)
#     print(line2_output)

with open("text1.txt", "r") as f:
    # r adalah read only
    line_by_line = f.readlines() 
    # print(line_by_line)
    # print(line_by_line[0])
    # print(line_by_line[1])
    for line in line_by_line:
        print(line)