import ssl
import socket
from datetime import datetime


def ssl_tls_checker(host, port=443):
    context = ssl.create_default_context()

    try:
        # Connect to host
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
        conn.settimeout(10.0)
        conn.connect((host, port))
        ssl_info = conn.getpeercert()
    except Exception as e:
        return f"Failed to connect or retrieve SSL certificate: {str(e)}"
    finally:
        if conn:
            conn.close()

    # Get certificate expiration
    expiration_date = datetime.strptime(ssl_info["notAfter"], "%b %d %H:%M:%S %Y GMT")
    days_remaining = (expiration_date - datetime.now()).days

    # Format issuer and subject
    issuer = {item[0][0]: item[0][1] for item in ssl_info["issuer"]}
    subject = {item[0][0]: item[0][1] for item in ssl_info["subject"]}

    result = {
        "Host": host,
        "Valid Until": expiration_date.strftime("%Y-%m-%d"),
        "Days Remaining": days_remaining,
        "Issuer": issuer,
        "Subject": subject,
        "Serial Number": ssl_info.get("serialNumber"),
        "Subject Alt Name": ssl_info.get("subjectAltName", "N/A"),
        "OCSP": ssl_info.get("OCSP", ("N/A",))[0],
        "CA Issuers": ssl_info.get("caIssuers", ("N/A",))[0],
        "CRL Distribution Points": ssl_info.get("crlDistributionPoints", ("N/A",))[0],
    }

    return result


def print_ssl_info(info):
    # Check if the info is a string (error message)
    if isinstance(info, str):
        print(info)
        return

    print("\nSSL/TLS Certificate Details:")
    print("-" * 40)
    for key, value in info.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for subkey, subvalue in value.items():
                print(f"  {subkey.ljust(20)}: {subvalue}")
        else:
            print(f"{key.ljust(20)}: {value}")
    print("-" * 40)


# Example usage
host = input("Give the website url: ")
info = ssl_tls_checker(host)
print_ssl_info(info)
