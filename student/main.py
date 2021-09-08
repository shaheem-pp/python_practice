# A teacher can add details of students of a class where each student have name, email & age.
# Teacher can add mark of Cs, Math & Eng. Also teacher want to add fee for each students.
# And at last teacher want to show all details.

# in this function we gets data of class name and strength. this strength can be used later.
#   when teacher want to enter details of each student

student_list = []
student_detail = {}


def welcome(class_name, strength_of_students):
    welcome_message = "Welcome to the Class \'" + class_name + "\' with \'" + str(
        strength_of_students) + "\' number of students"
    length_welcome_message = len(welcome_message)
    print(welcome_message)
    print(length_welcome_message * "*")


# after getting class and strength, ask teacher what he/she wanted to do
def ask_what_to_do():
    ask = "Enter Option number to do a task"
    length_ask = len(ask)
    print(ask)
    print((length_ask // 4) * "- - ")
    print("1) Enter Student Details ")
    print("2) Enter Mark of the Student")
    print("3) Enter Fee Details")
    print("4) Show Student Details")
    option = input("\tEnter a option(1 2 3 4): ")
    if option == 1:
        student_details()
    elif option == 2:
        student_mark()
    elif option == 3:
        fee_details()
    elif option == 4:
        print_details()
    else:
        print("Wrong Input :(")


def student_details():
    for i in range(strength_of_students):
        global student_detail
        student_detail = dict()
        student_detail["student_name"] = input("enter {}st student name: ".format(i + 1))
        student_detail["Age"] = input("enter {}st student age: ".format(i + 1))
        student_detail["email"] = (
                    student_detail["student_name"].replace(" ", "") + student_detail["Age"] + "@myCampus.edu").lower()
        student_list.append(student_detail)
    for _ in student_list:
        print("Student Name ->", student_detail["student_name"])
        print("Student Age ->", student_detail["Age"])
        print("Student Email ->", student_detail["email"])
        print()


def student_mark(self):
    print()

def fee_details(self):
    print()


def print_details(self):
    print()


class_name = input("Enter your class name: ").capitalize()
strength_of_students = int(input("Enter Number of Students: "))
welcome(class_name, strength_of_students)
student_details()
