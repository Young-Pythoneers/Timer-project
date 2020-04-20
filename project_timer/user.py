import binascii
import hashlib
import json
import os
from dataclasses import dataclass
import os.path
from os import path
from getpass import getpass


@dataclass
class User:
    """Class that stores the name and id of the user"""

    unique_id: str
    given_password: str


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


# correct_password, salt = get_employee_data()
# acces_check = password_comparrison(
#     correct_password, binascii.unhexlify(salt.encode()), "teddy"
# )  # teddy is the right password

#
# print(acces_check)


# def welcome(self):
#     return f"Welcome{self.name}, your ID is {self.id}"
##############################################################
##############################################################


def check_data_file():
    file_exists = path.exists("Employeess.json")
    if file_exists == False:
        # users = {} can maybe be used as overall dictionary
        with open("Employeess.json", "w") as outfile:
            pass
    else:
        pass


def check_user(emplyee_id):
    with open("Employeess.json", "r") as json_file:
        data = json.load(json_file)
        if emplyee_id not in data:
            print("Your account does'nt exist")
            create_user(emplyee_id)
        else:
            pass


# check_user("12")


def create_user(employee_id):
    # Maybe check correctness of data ??
    with open("Employeess.json", "w") as json_file:
        data = {}

        reply = (
            str(input("Do you want to create a new user," + " (y/n): ")).lower().strip()
        )
        if reply[:1] == "y":
            data[employee_id] = []
            first_name = str(input("Enter your first name: "))
            last_name = str(input("Enter your last name: "))
            password = getpass("Enter your password: ")
            encrypted_password, salt = create_password(password)

            data[employee_id].append(
                {
                    "first name": first_name,
                    "last name": last_name,
                    "password": encrypted_password,
                    "salt": salt,
                }
            )

            json.dump(data, json_file, indent=4)

        elif reply[:1] == "n":
            print("The application will now be closed")
        else:
            print("Invalid Input")
            return create_user(employee_id)

    # with open("Employeess.json", "r") as json_file:
    #     data = json.load(json_file)


# create_user("12")


check_data_file()
create_user("12")
