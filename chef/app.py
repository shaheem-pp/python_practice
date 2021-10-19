import string


class Chef:
    name: string
    hotel: string

    def introduce(name, hotel):

        print("Hello! I'm", name, "from", hotel)


def make_chicken(self):
    print("Make Chicken 65")


def make_rice(self):
    print("Make Fried rice")


def special_dish(self):
    print("Make Extre Cheesy Burger")


class Italian_chef(Chef):
    def special_dish(self):
        print("Parmessan Mac Cheese")

    def make_pizza(self):
        print("Chicken Cheese Pizza")


myChef = Chef

myChef.name = "Faiz"
myChef.hotel = "taj"

myChef.introduce()
