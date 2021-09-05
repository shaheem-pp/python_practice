a = 2
list = []
dictionary = {
    "student_name": "",
    "Age": "",
    "email": ""
}
for i in range(a):
    dictionary = dict()
    dictionary["student_name"] = input("enter student name: ")
    dictionary["Age"] = input("enter student age: ")
    dictionary["email"] = (dictionary["student_name"].replace(" ", "") + dictionary["Age"] + "@mycampus.com").lower()
    list.append(dictionary)

print(list)
#
# list = [
#     {
#         "student name": "Jane Foster",
#         "Age": "21",
#         "email": "fosterjane@gmail.com"
#     }, {
#         "student name": "Jane Foster",
#         "Age": "21",
#         "email": "fosterjane@gmail.com"
#     },
#     {
#         "student name": "Jane Foster",
#         "Age": "21",
#         "email": "fosterjane@gmail.com"
#     },
# ]
#
# for i in list:
#     print(i)
