import requests

# requests.post("https://ntfy.sh/mytopic",
#     data="Backup suck ses full 😀".encode(encoding='utf-8'))

requests.post("https://ntfy.sh/karkisa",
    data="An urgent message",
    headers={ "Priority": "2" })