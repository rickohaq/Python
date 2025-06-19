from scrapli.driver.core import EOSDriver
from scrapli.driver.generic import GenericDriver
import json
MY_DEVICE = [
    # {
    # "host": "192.168.20.230",  # Replace with your Arista device IP
    # "auth_username": "datacomm",
    # "auth_password": "D4t4c0mm",
    # "auth_secondary": "your_password",  # Optional, only needed if enable password is different
    # "auth_strict_key": False,      # Disable SSH key checking for lab/test
    # }, 
    # {
    # "host": "192.168.20.231",  
    # "auth_username": "datacomm",
    # "auth_password": "D4t4c0mm",
    # "auth_secondary": "your_password",  
    # "auth_strict_key": False,     
    # }, 
    # {
    # "host": "192.168.20.232",  
    # "auth_username": "datacomm",
    # "auth_password": "D4t4c0mm",
    # "auth_secondary": "your_password",  
    # "auth_strict_key": False,     
    # }, 
    # {
    # "host": "192.168.20.233",  
    # "auth_username": "datacomm",
    # "auth_password": "D4t4c0mm",
    # "auth_secondary": "your_password",  
    # "auth_strict_key": False,     
    # }, 
    # {
    # "host": "192.168.20.234",  
    # "auth_username": "datacomm",
    # "auth_password": "D4t4c0mm",
    # "auth_secondary": "your_password",  
    # "auth_strict_key": False,     
    # },
     {
    "host": "192.168.5.143",
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mmlt.6",
    "transport": "telnet",
    "auth_strict_key": False,
    "port": 23,
    # "platform": "generic",
    }
   
]

for device in MY_DEVICE:
    with GenericDriver(**device) as conn:
        # conn.channel.send_input("cli")  # Some devices need this to enter CLI mode
        response = conn.send_command("show version")
        print(response.result)