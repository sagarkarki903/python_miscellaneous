"""This program only takes the first five characters of the hashed password.
The API used here will return all the hashed passwords that has been hacked previously
with the number of time it has been hacked. We then can check the rest of our password
characters from our side to see if it matches them to perform a full check.
This way the API is never going to have all our password.
Basically, API gets our first five hashed password, and we check the rest from the returned
one to see if any matches! Cool!
"""

import requests
import hashlib


def request_api_data(first_five_hash):
    url = f'https://api.pwnedpasswords.com/range/{first_five_hash}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"{res.status_code}, milena")
    return res

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char = sha1password[:5]
    tail = sha1password[5:]
    response = request_api_data(first5_char)
    return get_pass_leak_count(response, tail)

def get_pass_leak_count(all_hacked, hash_to_check):

    for line in all_hacked.text.splitlines():
        list_separated_arr = line.split(":")

        if hash_to_check == list_separated_arr[0]:
            return f"*** HACKED {list_separated_arr[1]} times!!!!!!! ***"

    return "Safe! This password has not been hacked."


print(pwned_api_check(input("Enter the password you want to check: ")))