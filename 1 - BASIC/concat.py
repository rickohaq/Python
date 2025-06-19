command_string = input ("enter command : ")

command_to_send = "enable\n" + "conf t\n" +command_string + "\n" 
print (command_to_send)