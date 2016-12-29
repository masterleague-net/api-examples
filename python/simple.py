import requests  # http://python-requests.org/

# Premium user authentication process and API access example
r = requests.post('https://api.masterleague.net/auth/token/', data={'username': 'user', 'password': '12345'})

if 'token' not in r.json():
    print(r.text)
    raise ValueError("Unable to extract authentication token!")

token = r.json()['token']

s = requests.Session()
s.headers.update({'Authorization': 'Token ' + token})

r = s.get('https://api.masterleague.net/heroes.json')
print(r.text)

# Anonymous user access example
r = requests.get('https://api.masterleague.net/heroes.json')
print(r.text)
