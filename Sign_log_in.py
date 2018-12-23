from  Banner import banner
from Quetions import q_n_a

import sys
import getpass
import os.path


def make_account():
    banner()

    print("\tWELCOME,\n"
          "\tFor Sign In:\n"
          "\tENTER YOUR E-MAIL ID:", end='')

    em = input()

    filename = "username"
    with open(filename, "w") as f:
        f.write(em)

    pswd = getpass.getpass("\tENTER YOUR PASSWORD:")

    filename = "password"
    with open(filename, "w") as f:
        f.write(pswd)
    print("\n\tWant to Start quiz (Press 1/0) ..! :-", end='')
    i = int(input())
    if i == 1:
        q_n_a()
    else:
        sys.exit(0)


def login():
    banner()

    print("\tEnter registered Email id and Password,\n"
          "\tFor Log In:\n"
          "\tENTER YOUR E-MAIL ID:", end='')
    username = input()

    password = getpass.getpass("\tENTER YOUR PASSWORD:")

    if username == open("username").read() and password == open("password").read():
        print("\tSuccessful login")
        print("\n\tWant to Start quiz (Press 1/0) ..! :-", end='')
        i = int(input())
        if i == 1:
            q_n_a()
        else:
            sys.exit(0)

    else:
        print("\t\nThe email and password you entered did not match our records.\n "
              "\tPlease double-check and try again.\n")
        print("\tWant to try again or Exit? ( PRESS: 1 - RETRY, 0 - EXIT ):- ", end='')

        num = int(input())

        if num == 1:
            login()
        else:
            sys.exit(0)


def check_logs():
    if os.path.exists("username"):
        login()
    else:
        make_account()


if __name__ == '__main__':
    check_logs()
