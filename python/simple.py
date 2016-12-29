# coding: utf-8

import requests  # http://python-requests.org/

API_ROOT = 'https://api.masterleague.net'
API_USER = None
API_PASS = None

s = requests.Session()

if API_USER is not None and API_PASS is not None:
    r = requests.post(API_ROOT + '/auth/token/', data={'username': API_USER, 'password': API_PASS})
    if 'token' not in r.json():
        print(r.text)
        raise ValueError("Unable to extract authentication token!")

    token = r.json()['token']
    s.headers.update({'Authorization': 'Token ' + token})

r = s.get(API_ROOT + '/heroes.json')
print(r.text)
