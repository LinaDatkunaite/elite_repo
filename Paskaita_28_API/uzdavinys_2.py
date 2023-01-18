import csv

import requests
import json
API_key = '15ca09920cf07c884c7231ab9733cf6b'
ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91']
payload = ()
with open('countries.csv', 'a', newline='', encoding='utf-8') as f:
    writter=csv.writer(f,delimiter=',')
    writter.writerow(['IP', 'Country', 'Capital'])


    for i in ip_list:
        url = f'http://api.ipstack.com/{i}?access_key={API_key}'
        r = requests.get(url)
        data = json.loads(r.text)
        ip=(data["ip"])
        country_name=(data["country_name"])
        capital=(data["location"]['capital'])

        writter.writerow([ip, country_name, capital])
