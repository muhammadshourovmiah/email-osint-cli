# ------------------------------------------------------------------
# Developer : Muhammad Shourov (মোহাম্মদ সৌরভ)
# Facebook  : https://www.facebook.com/Junior.Writer.SHourov
# Module    : Gravatar Info Extractor
# ------------------------------------------------------------------

import hashlib
import requests

def get_gravatar(email):
    hash_email = hashlib.md5(email.strip().lower().encode()).hexdigest()
    url = f"https://www.gravatar.com/{hash_email}.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return None
