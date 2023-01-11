import requests

# GET METODAS - mes viska gaunam nuorodoj
# POST METODAS - paslepia kai kuriuos metodus

# r= requests.get('http://google.com/')
# print(r)
# print(dir(r))
# print(r.text)

# -------------------------------------
# r= requests.get('https://www.python.org/static/img/python-logo.png')
# print(r.content)
# with open('logo.png', 'wb') as f:
#     f.write(r.content)
# -------------------------------------

# stat cod - 200 request pavyko
# 500- serverio klaida
# 404 - tokio puslapio nera
# r= requests.get('https://www.python.org')
# print(r.status_code)

# 1. if r.status_code not in range (400, 600):
#     print("Pavyko prisijungti - tesiam darba")
# else:
#     print("Prisijungti nepavyko status kodas:", r.status_code)

# 2. tas pats kaip ir virsui tik su ok
# if r.ok:
#     print("Pavyko prisijungti - tesiam darba")
# else:
#     print("Prisijungti nepavyko status kodas:", r.status_code)

# -------------------------------------
# r= requests.get('https://www.python.org')
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.url)
# -------------------------------------
# r= requests.get('https://www.python.org/search/?q=pep')
# print(r.text)

# -------------------------------------
# payload = {'q': 'pep', 'page': 2}
# r= requests.get('https://www.python.org/search/', params=payload)
# print(r.text)
# print(r.url)


# -------------------------------------
# r= requests.post('http://httpbin.org/ip')
# print(r.text)
# -------------------------------------

# r= requests.get('http://httpbin.org/ip')
# print(r.text)
# -------------------------------------
# payload = {'name': 'Jonas', 'lastname': 'Jonaitis'}
# r= requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

