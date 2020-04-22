import binascii
import hashlib
import json
import os.path
import re
from dataclasses import dataclass
from getpass import getpass
from os import path


@dataclass
class User:
    """Data-class that stores employee_id of the user"""

    employee_id: str


def check_data_file() -> None:
    """Checks if an Employees.json file exists.

    The Employee.json file is needed to store all account information
    for persons that want to use this application.
    """
    file_exists = path.exists("Employees.json")
    if not file_exists:
        with open("Employees.json", "w") as outfile:
            data = {"Accounts": []}
            json.dump(data, outfile, indent=4)
    else:
        pass


def check_account_existence(employee_id: str) -> (str, str):
    """Checks if account already exists or not in Employees.json file.
    If not then create_account function is called, and if it does then
    the user will be verified based on a password comparison.

    Args:
        employee_id: This value is unique for every employee.

    """
    log_in_attempts = 0

    with open("Employees.json", "r") as json_file:
        data = json.load(json_file)

        if not any(employee_id in x for x in data["Accounts"]):
            print("Your account does'nt exist")
            create_user(employee_id)
        else:
            first_name, last_name, correct_password, correct_salt = get_employee_data(
                employee_id
            )
            put_in_password = create_password(
                getpass("Enter your password: "),
                binascii.unhexlify(correct_salt.encode()),
            )
            if put_in_password[0] == correct_password:
                logged_in(first_name, last_name)
                return first_name, last_name
            else:
                print("Sorry this password is not correct, please try again")
                log_in_attempts += 1
                check_account_existence(employee_id)
                if log_in_attempts == 3:
                    print(
                        "you're account will now be blocked, please try again in 5 minutes"
                    )


def create_user(employee_id: str) -> None:
    """Asks if you want to create an account for this application [y/n] question.
    if y: user needs to file in a first name, a last name and a password.
    if n: the application will be closed.
    if invalid answer: the user is asked again.

    Args:
        employee_id: This value is unique for every employee.
        all account data is stored under employee_id.


     """

    def append_account(data):
        """This function writes information of new account to Employees.json

        Args:
            data: Uses employee_id as key, values are:
                first name
                last name
                encrypted_password
                salt

        """
        with open("Employees.json", "w") as f:
            json.dump(data, f, indent=4)

    def password_length(password: str) -> str:
        """Checks if password meets all requirements

        Args:
            password: password that user wants to use for account.

        Returns:
            password: if password meets requirements it is returned.


        """

        print(
            "Password must contain at least:\n",
            "6-20 characters\n",
            "1 digit\n",
            "1 special character\n",
            "1 upper case and lowercase letter\n",
        )
        pswd_requirements = re.compile(
            "^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])"
        )
        meet_requirements = pswd_requirements.match(password)
        if meet_requirements:
            return password
        else:
            password_length(
                getpass("Your password is invalid please enter a password: ")
            )

    with open("Employees.json", "r") as json_file:
        data = json.load(json_file)
        temp = data["Accounts"]

        reply = (
            str(input("Do you want to create a new account," + " (y/n): "))
            .lower()
            .strip()
        )
        if reply[:1] == "y":
            length_temp = len(temp)
            temp.append({employee_id: []})

            first_name = str(input("Enter your first name: "))
            last_name = str(input("Enter your last name: "))

            password = password_length(getpass("Enter your password: "))
            encrypted_password, salt = create_password(password)
            temp[length_temp][employee_id].append(
                {
                    "first name": first_name,
                    "last name": last_name,
                    "password": encrypted_password,
                    "salt": salt,
                }
            )

        elif reply[:1] == "n":
            print("The application will now be closed")
        else:
            print("Invalid Input")
            return create_user(employee_id)

    append_account(data)
    check_account_existence(employee_id)


def create_password(pswrd: str, salt: bytes = os.urandom(32)) -> (str, str):
    """Creates hashed version of given password using a salt.

    Args:
        password: password for account.
        salt: Random byte needed to hash password.

    Returns:
        password: A str of the hashed password, this is necessary in order to store it in json format.
        salt: A str of salt, this is necessary in order to store it in json format.


    """
    key = hashlib.pbkdf2_hmac("sha256", pswrd.encode("utf-8"), salt, 100000)

    key_formatted = binascii.hexlify(key).decode()
    salt_formatted = binascii.hexlify(salt).decode()
    return key_formatted, salt_formatted


def get_employee_data(employee_id: str) -> (str, str, str, str):
    """Gets existing account data from the Employees.json file based on employee_id

    Args:
        employee_id: is used to search for correct account information

    Returns:
        first name: stored first name from Employees.json.
        last name: Stored last name from Employees.json.
        password: Stored password from Employees.json.
        salt: Stored salt from Employees.json.


    """

    with open("Employees.json") as json_file:
        data = json.load(json_file)
        for idx, user in enumerate(data["Accounts"]):
            if employee_id in user:
                for info in user[employee_id]:
                    return (
                        info["first name"],
                        info["last name"],
                        info["password"],
                        info["salt"],
                    )


def logged_in(first_name: str, last_name: str):
    """Displayes welcome message for now for the used

    Args:
        first_name: first name of user
        last_name: last name of user


    """

    print(f"Welcome {first_name} {last_name}, you're now logged in")
    # What do to once logged in ?
