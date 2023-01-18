import requests
import json
import csv

with open('weather.csv', 'a', newline='') as failas:
    writer = csv.writer(failas,
                        delimiter=',')  # susikuriame 'writer' objektą, nurodome kur rašysime, ir kad skirtukais bus kablelis
    writer.writerow(['IP', 'Country', 'City', 'Temp', 'Weather'])

ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174', '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']


API_weather = '106b58476ccda5f4170b15faab9be682'
API_IPbase = 'E7Gvn0x1YsB9bbjuz6tFhKpeG9DwFPIRpeETOV4G'



for ip in ip_list:

    url = f"https://api.ipbase.com/v2/info?ip={ip}&apikey={API_IPbase}"
    r = requests.get(url)
    data = json.loads(r.text)
    country = data['data']['location']['country']['name']
    city = data['data']['location']['city']['name']
    lat = data['data']['location']['latitude']
    long = data['data']['location']['longitude']
    payload = {'units': 'metric'}
    # url2 =  f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_weather}'
    url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_weather}'
    r1 = requests.get(url2, params=payload).text
    data2 = json.loads(r1)
    print(data2)
    temperature = (data2['main']['temp'])
    weather = (data2['weather'][0]['main'])

    l=[ip, country, city, temperature, weather]

    with open('weather.csv', 'a', newline='', encoding='utf-8') as failas:
        writer = csv.writer(failas, delimiter=',')
        writer.writerow(l)
