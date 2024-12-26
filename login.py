import os
import requests

os.system('cls' if os.name == 'nt' else 'clear')

username = input("[+] Enter Username: ")
password = input("[+] Enter Password: ")
print()

url = "https://ajax.streamable.com/check"

data = {
    "username": username,
    "password": password 
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
}

r = requests.post(url, json=data).json()

if "ad_tags" in r:
    print(f"Logged in successfully! Plan={r['plan_name']}, Videos={r['total_videos']}, Country={r['country']}")
else:
    print(f"Bad Login! {r['message']}")
