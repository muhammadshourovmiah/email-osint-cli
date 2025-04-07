# ------------------------------------------------------------------
# Developer : Muhammad Shourov (মোহাম্মদ সৌরভ)
# Facebook  : https://www.facebook.com/Junior.Writer.SHourov
# Project   : Email OSINT CLI Tool
# ------------------------------------------------------------------

from utils.validate import validate
from utils.domain_info import get_mx_records
from utils.breach_check import check_breach
from utils.gravatar import get_gravatar

def main():
    print("=== Email OSINT CLI Tool ===")
    email = input("Enter target email: ").strip()

    print("\n[+] Validating email...")
    if validate(email):
        print("    --> Email is valid.")
    else:
        print("    --> Email is invalid or unreachable.")

    domain = email.split('@')[-1]
    print(f"\n[+] Checking MX records for domain: {domain}")
    mx = get_mx_records(domain)
    print(f"    --> MX Records: {mx}")

    print("\n[+] Checking data breaches...")
    breaches = check_breach(email)
    if breaches is None:
        print("    --> Error fetching breach data.")
    elif breaches == []:
        print("    --> No breaches found.")
    else:
        for breach in breaches:
            print(f"    --> Breach: {breach['Name']}")

    print("\n[+] Checking Gravatar profile...")
    gravatar = get_gravatar(email)
    if gravatar:
        entry = gravatar['entry'][0]
        print(f"    --> Name: {entry.get('displayName', 'N/A')}")
        print(f"    --> Profile: {entry.get('profileUrl', 'N/A')}")
    else:
        print("    --> No Gravatar profile found.")

if __name__ == "__main__":
    main()
