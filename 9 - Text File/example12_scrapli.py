from scrapli.driver.core import EOSDriver

MY_DEVICE = {
    "host": "192.168.20.230",  # Replace with your Arista device IP
    "auth_username": "datacomm",
    "auth_password": "D4t4c0mm",
    "auth_secondary": "your_password",  # Optional, only needed if enable password is different
    "auth_strict_key": False,      # Disable SSH key checking for lab/test
}
from datetime import datetime
my_time=datetime.now().strftime("%H:%M:S")
command_to_send = input ("Enter the command you wish to send: ")
# Open connection
with EOSDriver(**MY_DEVICE) as conn:
    response = conn.send_command(command_to_send)

my_list = response.result.splitlines()  #it will make the show running into a list

with open(f"{command_to_send}-{my_time}.txt", "x") as f:
    for line in my_list:
        f.write(line + "\n")


# In Python' s open() function, the "x" file mode means:

# ✅ Create a new file and open it for writing.
# ❌ If the file already exists, it will raise a FileExistsError.