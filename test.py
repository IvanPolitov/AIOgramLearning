import re
import requests
import time

TOKEN = ""
API_URL = "https://api.telegram.org/bot"
with open("secret.txt", "r") as q:
    text = q.read()
    TOKEN = re.match(r'token:([:\w-]*$)', text).group(1)
for i in range(1000):
    updates = requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id=1393291388&text=QQQQQQQ')
    print(updates.text)
    time.sleep(1)
