import random as rand


def get_names(num):
    names = list()
    for i in range(0, num):
        names.append(input("Enter a name: "))
    return names


def get_number_of_people():
    return int(input("Enter number of People"))


def get_num_of_teams():
    return int(input("Enter number of teams: "))


num = get_number_of_people()
names = get_names(num)
teams = get_num_of_teams()
strength = int(num / teams)
members = list()

while num >= 0:
    for i in range(0, teams):
        if len(members) <= strength:
            person = rand.randint(0, len(names))
            members.append(names[person])
            names.remove(names[person])
        print(members)
        num = num - strength
