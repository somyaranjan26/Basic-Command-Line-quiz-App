from Banner import banner

begi_level = "Beginner Level"
basic_level = "Basic Level"
advance_level = "Advance level"

questions = [begi_level, basic_level, advance_level]

quiz = {
    begi_level: [("1.	Which of the following statements is used to create an empty set?"
                  "\n\t1)	{ }"
                  "\n\t2)	set()"
                  "\n\t3)	[ ]."
                  "\n\t4)	( )", 2),

                 ("2.   If a={5,6,7,8}, which of the following statements is false?"
                  "\n\t1)	print(len(a))"
                  "\n\t2)	print(min(a))"
                  "\n\t3)	a.remove(5)"
                  "\n\t4)	a[2]=45", 4),

                 ("3.   If a={5,6,7}, what happens when a.add(5) is executed?"
                  "\n\t1)	a={5,5,6,7}"
                  "\n\t2)	a={5,6,7}"
                  "\n\t3)	Error as there is no add function for set data type"
                  "\n\t4)	Error as 5 already exists in the set", 4)],

    basic_level: [("1.	Which of the following is not the correct syntax for creating a set?"
                   "\n\t1)	set([[1,2],[3,4]])"
                   "\n\t2)	set([1,2,2,3,4])"
                   "\n\t3)	set((1,2,3,4))"
                   "\n\t4)	{1,2,3,4}", 1),

                  ("2.  Which of the following functions will not result in an error "
                   "when no arguments are passed to it?"
                   "\n\t1)  min()"
                   "\n\t2)  divmod()"
                   "\n\t3)  all()"
                   "\n\t4)  float()", 4),

                  ("3.  Which of the following statements are true?"
                   "\n\t1)  When you open a file for reading, if the file does not exist, an error occurs"
                   "\n\t2)  When you open a file for writing, if the file does not exist, a new file is created"
                   "\n\t3)  When you open a file for writing, if the file exists, "
                   "the existing file is overwritten with the new file"
                   "\n\t4) All of the mentioned", 4)],

    advance_level: [("1.   Which of these about a set is not true?"
                     "\n\t1)   Mutable data type"
                     "\n\t2)   Allows duplicate values"
                     "\n\t3)   Data type with unordered values"
                     "\n\t4)   Immutable data type", 4),

                    ("2.   Which is the most appropriate definition for recursion?"
                     "\n\t1)   A function that calls itself"
                     "\n\t2)   A function execution instance that calls another execution instance of the same function"
                     "\n\t3)   A class method that calls another class method"
                     "\n\t4)   An in-built method that is automatically called", 2),

                    ("3.   What are the methods which begin and end with two underscore characters called?"
                     "\n\t1)   Special methods"
                     "\n\t2)   In-built methods"
                     "\n\t3)   User-defined methods"
                     "\n\t4)   Additional methods", 1)]
}

result = {"Correct": 0, "Incorrect": 0}


def get_quiz_choice():
    while True:
        try:
            print("\n * Choose the quiz  level you like\n1 for {}\n2 for {}\n3 for {}\n"
                  "\tYour choice:".format(begi_level, basic_level, advance_level))
            quiz_number = int(input())
        except ValueError:
            print("\tNot a number, please try again\n")
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print("\tInvalid value, please try again\n")
            else:
                return quiz_number


def get_answer(question, correct_answer):
    while True:
        try:
            print("Q: {}".format(question))
            answer = int(input("\n\tYour answer: "))
        except ValueError:
            print("\n\tNot a number, please try again\n")
        else:
            if answer is not 1 and answer is not 2 and answer is not 3 and answer is not 4:
                print("\n\tInvalid value, please try again\n")
            elif answer is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False


def q_n_a():
    banner()

    choice = get_quiz_choice()
    quiz_name = questions[choice - 1]
    print("\nYou chose the {}".format(quiz_name))
    print(end='')
    quiz_questions = quiz[quiz_name]
    for q in quiz_questions:
        print("\tYour answer is: {}\n".format(str(get_answer(q[0], q[1]))))
    print("\n\tYour SCORE: {}".format(result))
    print("\n\tHOPE U ENJOYED! :-)")


if __name__ == '__main__':
    q_n_a()
