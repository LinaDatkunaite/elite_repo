
import requests
import json



people = requests.get('https://www.travel-advisory.info/api?')
# print(type(people.text), people.text)
info_json = json.loads(people.text)
countries = info_json['data']
for i in countries:
    country = countries[i]
    print('')
    print(country['name'], country['advisory']['score'], country['advisory']['message'])
