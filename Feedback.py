from Banner import banner


def feedback():

    banner()

    f = open("Feedback.txt", "a")
    print("\t\nPlease Enter Your Feedback: ", end='')
    f.write(input())
    print("Thank You for your Feedback!")


if __name__ == '__main__':
        feedback()

