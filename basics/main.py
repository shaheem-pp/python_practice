import datetime

print("Hello World")

name = "Shaheem PP"
age = -1

print("I\'m " + name)
print(f"I\'m {age} years old")

if age >= 18:
	print("Welcome to Adulthood. It is not that good but you gonna love it!")
elif age < 18 and age >= 14:
	print("Oops, you are not eligible for driving license")
elif age < 0:
	print("Dude, come on there is no negative age!")
else:
	print("You should go to school now")

for i in range(1, 11):
	print(i, end = "")
print()
for i in range(10):
	print(i, end = "")
print()

# number = []
# for i in range(1, 26):
# 	number.append(i)
#
# names = ["Adam (peace be upon him)", "Idris (Enoch, peace be upon him)", "Nuh (Noah, peace be upon him)",
#          "Hud (peace be upon him)", "Salih (peace be upon him)", "Ibrahim (Abraham, peace be upon him)",
#          "Lut (Lot, peace be upon him)", "Ismail (Ishmael, peace be upon him)", "Ishaq (Isaac, peace be upon him)",
#          "Yaqub (Jacob, peace be upon him)", "Yusuf (Joseph, peace be upon him)", "Ayyub (Job, peace be upon him)",
#          "Shuayb (Jethro, peace be upon him)", "Musa (Moses, peace be upon him)", "Harun (Aaron, peace be upon him)",
#          "Dawud (David, peace be upon him)", "Sulayman (Solomon, peace be upon him)",
#          "Ilyas (Elijah, peace be upon him)", "Al-Yasa (Elisha, peace be upon him)", "Yunus (Jonah, peace be upon him)",
#          "Zakariyya (Zechariah, peace be upon him)", "Yahya (John the Baptist, peace be upon him)",
#          "Isa (Jesus, peace be upon him)", "Muhammad (peace be upon him)", "Dhul-Kifl (Ezekiel, peace be upon him)"]
#
# for num, name in zip(number, names):
# 	if len(num)==1:
# 		num = "0"+num
# 	print(num, "-", name)

names = ["Adam (peace be upon him)", "Idris (Enoch, peace be upon him)", "Nuh (Noah, peace be upon him)",
         "Hud (peace be upon him)", "Salih (peace be upon him)", "Ibrahim (Abraham, peace be upon him)",
         "Lut (Lot, peace be upon him)", "Ismail (Ishmael, peace be upon him)", "Ishaq (Isaac, peace be upon him)",
         "Yaqub (Jacob, peace be upon him)", "Yusuf (Joseph, peace be upon him)", "Ayyub (Job, peace be upon him)",
         "Shuayb (Jethro, peace be upon him)", "Musa (Moses, peace be upon him)", "Harun (Aaron, peace be upon him)",
         "Dawud (David, peace be upon him)", "Sulayman (Solomon, peace be upon him)",
         "Ilyas (Elijah, peace be upon him)", "Al-Yasa (Elisha, peace be upon him)", "Yunus (Jonah, peace be upon him)",
         "Zakariyya (Zechariah, peace be upon him)", "Yahya (John the Baptist, peace be upon him)",
         "Isa (Jesus, peace be upon him)", "Muhammad (peace be upon him)", "Dhul-Kifl (Ezekiel, peace be upon him)"]

for num, name in enumerate(names, start = 1):
	num_str = str(num).zfill(2)  # zero-pad the number
	print(f"{num_str} - {name}")

# enumerate will go through names, and index will be stores in num. the start parameter sets from where it should start
# zfill sets 0 on the left side of the value to make the size same


# ----------------------------------------------------------------------------------------------------------------------


i = 0
while ("Ezekiel" not in names[i]):
	print(names[i])
	i = i + 1

print()
print()
print("------------------------------------------")
print()
print()

fruits_list = list()
fruits_list.append("Apple")
fruits_list.append("mango")
fruits_list.append("Orange")
print(fruits_list)
fruits_list.sort()
print(fruits_list)
fruits_list.sort(reverse = True)
print(fruits_list)
print("length of list =", len(fruits_list))
for i in ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]:
	fruits_list.append(i)
fruits_list.sort()
print(fruits_list)
print(fruits_list[2:5])  # m to n+1
fruits_list.insert(2, "watermelon")
print(fruits_list)
fruits_list.pop()
print(fruits_list)
fruits_list.pop(3)
print(fruits_list)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# append()  -   Adds an element at the end of the list
# clear()	-   Removes all the elements from the list
# copy()	-   Returns a copy of the list
# count()	-   Returns the number of elements with the specified value
# extend()	-   Add the elements of a list (or any iterable), to the end of the current list
# index()	-   Returns the index of the first element with the specified value
# insert()	-   Adds an element at the specified position
# pop()	    -   Removes the element at the specified position
# remove()	-   Removes the item with the specified value
# reverse()	-   Reverses the order of the list
# sort()	-   Sorts the list


print()
print()
print("------------------------------------------")
print()
print()

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
type_choices = ((0, 'No Special Access'), (1, 'Admin'))
print(type_choices)

print()
print()
print("------------------------------------------")
print()
print()

myset = {"apple", "banana", "cherry"}
print(myset)

print()
print()
print("------------------------------------------")
print()
print()

thisdict = {
		"brand": "Ford",
		"model": "Mustang",
		"year": 1964
}
print(thisdict)

print()
print()
print("------------------------------------------")
print()
print()


def add(a, b):
	print(a + b)


def sub(a, b):
	return (a - b)


def mul():
	print(10 * 10)


def div():
	return 100 / 10


add(1, 2)
subs = sub(2, 1)
print(subs)
mul()
divs = div()
print(divs)

print()
print()
print("------------------------------------------")
print()
print()


class Person():

	def __init__(self, name, language):
		self.name = name
		self.language = language

	def say_hello(self):
		print(self.name, "says hello!")

	def my_language(self):
		print("I can speak in", self.language)


class Student(Person):

	def __init__(self, name, language, graduation_year):
		super().__init__(name, language)
		self.graduation_year = graduation_year

	def say_hello(self):
		print("Hi, I'm", self.name, "I'm happy to welcome you to our school!")

	def which_year(self):
		year = datetime.date.today().year
		if self.graduation_year > year:
			print("I'm", self.graduation_year - year, "year to my graduation")
		else:
			print("I'm graduated")


shan = Person(name = "Shaheem", language = "Malayalam")
shan.say_hello()
shan.my_language()

naswih = Student(name = "Naswih", language = "English", graduation_year = 2024)
naswih.say_hello()
naswih.my_language()
naswih.which_year()
