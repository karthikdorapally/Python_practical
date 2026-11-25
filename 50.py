
import subprocess
import platform

ip = input("Enter IP Address: ")

param = "-n" if platform.system().lower() == "windows" else "-c"

command = ["ping", param, "1", ip]

result = subprocess.run(
    command,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

if result.returncode == 0:

    print(ip, "is UP")

else:

    print(ip, "is DOWN")    
