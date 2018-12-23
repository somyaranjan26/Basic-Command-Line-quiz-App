from Banner import banner
from Start_Page import start_quiz
from Sign_log_in import check_logs
from Feedback import feedback
from About_Sec import about_sec
import os as o
import sys


o.system("clear")


def hello():

    banner()
    print("\t******************************************************************\n")

    print("\tSELECT ANY ONE CHOICE:\n"
          "\t        1. Start Quiz\n"
          "\t        2. Resume Quiz\n"
          "\t        3. Feedback\n"
          "\t        4. About Application\n"
          "\t        5. Exit\n"
          "\tENTER YOUR CHOICE HERE:- ", end='')

    var = int(input())

    if var == 1:
        start_quiz()
    elif var == 2:
        check_logs()
    elif var == 3:
        feedback()
    elif var == 4:
        about_sec()
    elif var == 5:
        print("Thank you Using!")
        sys.exit(0)


if __name__ == '__main__':
    hello()
