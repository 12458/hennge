import requests
import hmac
import hashlib
import time
import struct


def get_totp_token(secret, intervals_no):
    key = secret.encode()
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha512).digest()
    o = o = h[len(h) - 1] & 15
    h = struct.unpack('>I', h[o:o+4])[0] & 0x7fffffff
    return str(h)[-10:].zfill(10)


def generate_totp(email):
    secret = email + "HENNGECHALLENGE003"
    intervals_no = int(time.time()) // 30
    return get_totp_token(secret, intervals_no)


data = {
    "github_url": "[YOUR GIST URL HERE]",
    "contact_email": "[YOUR EMAIL HERE]",
    "solution_language": "python"
}
headers = {"Content-Type": "application/json"}
# Generate TOTP
totp = generate_totp(data["contact_email"])

url = "https://api.challenge.hennge.com/challenges/003"

response = requests.post(url, json=data, headers=headers, auth=(data["contact_email"], totp))

print(response.status_code)
print(response.text)
print(response.raw)
