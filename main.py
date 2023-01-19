import time
import pyotp
import qrcode

#  key = pyotp.random_base32()
key = "supersecretkey"

#totp = pyotp.totp(key)

# print(totp.now())
#
# time.sleep(30)
#
# print(totp.now())
#
# input_code = input("enter 2fa code:")
# totp.verify(input_code)
# print(totp.verify(input_code))
#
# # counter based passwords
# counter = 0
# hotp = pyotp.hotp(key)
#
# print(hotp.at(0))
# print(hotp.at(1))
# print(hotp.at(2))
# print(hotp.at(3))
# print(hotp.at(4))
#
# for _ in range(5):
#     print(hotp.verify(input("enter code:"),counter))
#     counter += 1

# QR code that can be scanned by an authernticator app QR COE pip install qrcode
totp = pyotp.totp(key)
uri = pyotp.totp.TOTP(key).provisioning_uri(name="MikeSmith5087", issuer_name="APP_Name")
print(uri)

qrcode.make(uri).save("totp.png")


totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter code:")))
