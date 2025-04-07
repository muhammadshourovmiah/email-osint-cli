# ------------------------------------------------------------------
# Developer : Muhammad Shourov (মোহাম্মদ সৌরভ)
# Facebook  : https://www.facebook.com/Junior.Writer.SHourov
# Module    : Email Validation
# ------------------------------------------------------------------

from validate_email_address import validate_email

def validate(email):
    is_valid = validate_email(email, verify=True)
    return is_valid
