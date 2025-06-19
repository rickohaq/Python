from scrapli import Scrapli

# Device connection parameters
device = {
    "host": "192.168.20.230",  # Replace with your Arista device IP
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mm",
    "auth_strict_key": False,
    "platform": "arista_eos",  # IMPORTANT: use the correct platform
    "transport": "paramiko",  # "ssh2" is recommended for speed, "paramiko" also works
}

from datetime import datetime
my_time=datetime.now().strftime("%H:%M:S")
print(my_time)
# Connect and run the command
conn = Scrapli(**device)
conn.open()

response = conn.send_command("show version")

print(response.result)

conn.close()
