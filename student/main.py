# A teacher can add details of students of a class where each student have name, email & age.
# Teacher can add mark of Cs, Math & Eng. Also teacher want to add fee for each students.
# And at last teacher want to show all details.

class Student:
    student_list = []
    student_detail = {
        "student_name": "",
        "Age": "",
        "email": ""
    }

    # in this function we gets data of class name and strength. this strength can be used later.
    #   when teacher want to enter details of each student
    def __init__(self, class_name, strength_of_students):
        self.class_name = class_name
        self.strength_of_students = strength_of_students
        welcome_message = "Welcome to the Class \'" + self.class_name + "\' with \'" + str(
            strength_of_students) + "\' number of students"
        length_welcome_message = len(welcome_message)
        print(welcome_message)
        print(length_welcome_message * "*")

    # after getting class and strength, ask teacher what he/she wanted to do
    def ask_what_to_do(self):
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
            self.student_details()
        elif option == 2:
            self.student_mark()
        elif option == 3:
            self.fee_details()
        elif option == 4:
            self.print_details()
        else:
            print("Wrong Input :(")

    def student_details(self):
        student_list = []
        student_detail = {
            "student_name": "",
            "Age": "",
            "email": ""
        }
        while self.strength_of_students != 0:
            print("Enter Detail of Student 1")
            student_detail["student_name"] = input("enter student name: ")
            student_detail["Age"] = input("enter student age: ")
            student_detail["email"] = (student_detail["student_name"].replace(" ", "") + student_detail[
                "Age"] + "@mycampus.com").lower()
            student_list.append(student_detail)

            self.strength_of_students = self.strength_of_students - 1

        for i in student_list:
            print(student_list)

    def student_mark(self):
        print()

    def fee_details(self):
        print()

    def print_details(self):
        print()


class_name = input("Enter your class name: ")
strength_of_students = int(input("Enter Number of Students: "))

s1 = Student(class_name, strength_of_students)
s1.student_details()
