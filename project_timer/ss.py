import re
from getpass import getpass


def password_length(password: str) -> str:
    """Checks if password meets all requirements

    Args:
        password: password that user wants to use for account

    Returns:
        password: if password meets requirements it is returned


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

        password_length(getpass("Your password is invalid please enter a password: "))


password_length("a")
