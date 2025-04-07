# ------------------------------------------------------------------
# Developer : Muhammad Shourov (মোহাম্মদ সৌরভ)
# Facebook  : https://www.facebook.com/Junior.Writer.SHourov
# Module    : Domain Info Checker
# ------------------------------------------------------------------

import dns.resolver

def get_mx_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return [str(rdata.exchange) for rdata in answers]
    except Exception as e:
        return [f"Error: {e}"]
