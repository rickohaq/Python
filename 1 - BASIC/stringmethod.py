platform = input ("what is your platform" )
show_command = input ("what show command do you want to send? ")
platform_to_test = platform.lower()

if platform == "arista":
    cli = f"enable\n {show_command}\n"
    print(cli)
    # else:
    # print("not arista switches")