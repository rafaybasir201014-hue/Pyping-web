import requests
import time
print("Starting pyping-web testing")
time.sleep(1)
print("-" * 40)
time.sleep(1)
try:
        with open("targets.list","r") as file:
            targets=file.read().splitlines()
except FileNotFoundError:
    print("No targets.list file found")
    targets=["https://www.google.com"]
for url in targets:
    if not url.strip():
        continue
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print("This url is online!")
        else:
            print("This url is not online!")
    except requests.exceptions.ConnectionError:
                    print("This url is not online!")



