import re


def phishing_url_check(url):
    suspicious_patterns = [
        r"[-_][a-zA-Z0-9]{1,}@?",  # Domain impersonation
        r"\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}",  # IP in the domain part
        r"(login|verify|account|secure|update|auth)\.",  # Common phishing words
        r"(\.com-|\.net-|\.org-|\.ru-|\.info-|\.co\.uk-)",  # Dash after top-level domain
        r"([a-zA-Z0-9-]+\.)+\d{1,3}",  # Domain name ending in numbers
        r"https?://[a-zA-Z0-9-.]+[a-zA-Z0-9-]{60,}",  # Long domain names
    ]

    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return "Attention! Potential phishing URL detected: " + url

    return "URL appears to be safe."


# Testing List
test_url_list = [
    "http://www.google.com-verify-account.secure.com",
    "http://192-168-1-1-secure.com",
    "http://update-facebook-info.com",
    "http://bankofamerica.secure-login.verify-credentials.com",
    "http://safe.com",
]

manualinput = input("Do you want to give a url? (y/n) ")
if manualinput == "y":
    print(phishing_url_check(input("Give url: ")))
else:
    for url in test_url_list:
        print(phishing_url_check(url))
