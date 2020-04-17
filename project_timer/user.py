import binascii
import hashlib
import json
import os
from dataclasses import dataclass
from random import randint


@dataclass
class User:
    """Class that stores the name and id of the user"""

    name: str
    id: int = randint(1, 100)

    def welcome(self):
        return f"Welcome{self.name}, your ID is {self.id}"


##########################################


def create_password(pswrd, salt=os.urandom(32)):
    password = pswrd

    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)

    key_formatted = binascii.hexlify(key).decode()
    salt_formatted = binascii.hexlify(salt).decode()
    return key_formatted, salt_formatted


pswd, slt = create_password(
    "teddy",
    b"\xb5\xefgoQ\xc5\xe1\xea\x8e\x86\xf2\x9f\x17\xd8qe\x0b\x17\x02\xd3$.\xf0\xcf\x8fQ\xa7Z\x8a\xdc\x9c/",
)


def get_employee_data():  # needs id as input
    with open("Employees.json") as json_file:
        data = json.load(json_file)
        for attributes in data["30014"]:
            return attributes["password"], attributes["salt"]


def password_comparrison(correct_password, salt, given_passwords):
    pswd = create_password(given_passwords, salt)
    if pswd[0] == correct_password:
        return "you're most welcome"
    else:
        return "Youre a filthy liar go away"


correct_password, salt = get_employee_data()
acces_check = password_comparrison(
    correct_password, binascii.unhexlify(salt.encode()), "teddy"
)  # teddy is the right password

print(acces_check)
