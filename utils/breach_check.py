# ------------------------------------------------------------------
# Developer : Muhammad Shourov (মোহাম্মদ সৌরভ)
# Facebook  : https://www.facebook.com/Junior.Writer.SHourov
# Module    : Data Breach Checker (HIBP)
# ------------------------------------------------------------------

import requests

def check_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "User-Agent": "email-osint-cli",
        "hibp-api-key": "YOUR_HIBP_API_KEY"
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 404:
            return []
        else:
            return None
    except:
        return None
