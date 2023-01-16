import requests
import json

# people = requests.get('http://api.open-notify.org/astros.json')
# print(type(people.text), people.text)
#
# info_json = json.loads(people.text)
# print(info_json)
# print(info_json['people'])
#
# for i in info_json['people']:
#     print(i['name'])
#
#
#
#
# import webbrowser as wb
# import requests
# import json
#
# API_key = '14795746-624081efd179b5bd9be0efe43'
#
#
# def open_first(query):
#    payload = {'key': API_key, 'q': query, 'img_type': 'photo', 'pretty': 'true'}
#    r = requests.get('https://pixabay.com/api/', params=payload)
#    json_str = r.text
#    result = json.loads(json_str)
#    wb.open_new_tab(result['hits'][1]['largeImageURL'])
#
# open_first('elephant')


# EXC 1 Sukurkite programą, kuri duoda įvestos valiutų poros dabartinį kursą. Naudokitės https://api.frankfurter.app/.
# Dokumentaciją rasite Čia. Rezultatas galėtų atrodyti taip:

# def get_rate(from_currency, to_currency):
#     currencies_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR',
#                        'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK',
#                        'SGD', 'THB', 'TRY', 'USD', 'ZAR']
#
#     if from_currency not in currencies_list or to_currency not in currencies_list:
#         print("Curriencies inserted not found")
#     else:
#         try:
#             r = requests.get(f'https://api.frankfurter.app/latest?from={from_currency}')
#             print(r.status_code)
#             currency_dict = json.loads(r.text)
#             rate=currency_dict['rates'][f'{to_currency}']
#             print(f'{from_currency}-{to_currency}:\t{rate}')
#         except KeyError:
#             print("You inserted same currencies")
#
# get_rate('CAD', 'CAD')


# EXC 3 Naudodami tą pačią Frankfurter API (kaip ir pirmoje užduotyje), sukurkite programą,
# kuri pagal parametruose pateiktas valiutų poras, periodo pradžios ir pabaigos datą surastų
# dienas kai kursas buvo aukščiausias ir kai kursas buvo žemiausias Maždaug taip:

import datetime

def currency_pair_analysis(curr1, curr2, start_date, end_date):
    exchange_r_dict = {}
    payload = {'base': curr1}
    r = requests.get(f'https://api.frankfurter.app/{start_date}..{end_date}', params=payload)
    currencies_dict = json.loads(r.text)
    curr_dict=currencies_dict['rates']


    date_time_start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    date_time_end = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    for i in range((date_time_end - date_time_start).days + 1):
        date = (date_time_start + datetime.timedelta(i)).date()
        if date.weekday() not in (5, 6):
            weekdays_rate=curr_dict[str(date)][curr2]
            # print(date, weekdays_rate)
            exchange_r_dict[f'{date}'] = weekdays_rate

    max_value = max(exchange_r_dict.values())
    max_key = max(exchange_r_dict, key=exchange_r_dict.get)
    min_value = min(exchange_r_dict.values())
    min_key = min(exchange_r_dict, key=exchange_r_dict.get)

    print(f"For currencies {curr1}-{curr2}, in period {start_date} to {end_date}:\nLowest exchange rate was {min_key} - {min_value}\n"
          f"Highest exchange rate was {max_key} - {max_value}")


currency_pair_analysis(curr1='EUR', curr2='AUD', start_date='2023-01-01', end_date='2023-01-16')


# import requests
#
# sign_list = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
#
#
# def horoscope_tomorrow(sign):
#     params = (
#         ('sign', sign),
#         ('day', 'tomorrow'),
#     )
#     if sign not in sign_list:
#         print("Sign not found. Try again")
#     else:
#         r = requests.post('https://aztro.sameerkumar.website/', params=params)
#         horoscope_dict = json.loads(r.text)['description']
#         print(F'Tomorrows horoscope for {sign} is:\n{horoscope_dict}')
#
#
# horoscope_tomorrow('scorpio')
