from Sign_log_in import *
from Banner import banner
import sys


def start_quiz():
    banner()

    print("\n\t~ If You Are New User, "
          "Please Sign In First,"
          "And Then Log In..\n")

    print("\tSelect Any One Option: \n"
          "\t     1. Sign In \n"
          "\t     2. Log In \n"
          "\t     3. Exit\n"
          "\tEnter Your Choice:- ", end='')

    check = int(input())

    if check == 1:
        check_logs()
    elif check == 2:
        check_logs()
    elif check == 3:
        sys.exit(0)
    else:
        print("\tEnter Valid Key (i.e. 1, 2 or 3)")


if __name__ == "__main__":
    start_quiz()
