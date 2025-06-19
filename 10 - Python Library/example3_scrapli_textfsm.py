from scrapli.driver.core import EOSDriver
import json
MY_DEVICE = [
    {
    "host": "192.168.20.230",  # Replace with your Arista device IP
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mm",
    "auth_secondary": "your_password",  # Optional, only needed if enable password is different
    "auth_strict_key": False,      # Disable SSH key checking for lab/test
    }, 
    {
    "host": "192.168.20.231",  
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mm",
    "auth_secondary": "your_password",  
    "auth_strict_key": False,     
    }, 
    {
    "host": "192.168.20.232",  
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mm",
    "auth_secondary": "your_password",  
    "auth_strict_key": False,     
    }, 
    {
    "host": "192.168.20.233",  
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mm",
    "auth_secondary": "your_password",  
    "auth_strict_key": False,     
    }, 
    {
    "host": "192.168.20.234",  
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mm",
    "auth_secondary": "your_password",  
    "auth_strict_key": False,     
    },
]

command_to_send = input ("Enter the command you wish to send: ")
for DEVICE in MY_DEVICE:
    with EOSDriver(**DEVICE) as conn:
        response = conn.send_command(command_to_send)
        # structured_result = response.textfsm_parse_output()
        structured_result = json.dumps(response.textfsm_parse_output(),indent=2) #it will make more easier to read but also make it to string
    print(structured_result)
    print("\n\n\n")    
    # print(dir(response))
