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

for DEVICE in MY_DEVICE:
    with EOSDriver(**DEVICE) as conn: #EOSDriver buat enable dan conf t
        response = conn.send_configs_from_file("config.cfg")