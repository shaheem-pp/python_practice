# import random as rand
#
#
# def get_names(num):
#     names = list()
#     for i in range(0, num):
#         names.append(input("Enter a name: "))
#     return names
#
#
# def get_number_of_people():
#     return int(input("Enter number of People"))
#
#
# def get_num_of_teams():
#     return int(input("Enter number of teams: "))
#
#
# num = get_number_of_people()
# names = get_names(num)
# teams = get_num_of_teams()
# strength = int(num / teams)
# members = list()
#
# while num >= 0:
#     for i in range(0, teams):
#         if len(members) <= strength:
#             person = rand.randint(0, len(names))
#             members.append(names[person])
#             names.remove(names[person])
#         print(members)
#         num = num - strength

# First, we'll import the random module to help us shuffle the players
import random

# Next, we'll define the number of teams and the number of players per team
players_per_team = 4

# Then, we'll create a list of all the players that we want to include in the teams
players = []
for i in range(47):
    players.append("player " + str(i))

# Now, we'll shuffle the players so that they are in a random order
random.shuffle(players)

# Finally, we'll generate the teams by grouping the players into sublists of the desired size
teams = [players[i:i + players_per_team] for i in range(0, len(players), players_per_team)]

# Print the teams to verify that they were generated correctly
for i in range(len(teams)):
    print("Team", i + 1, "->", teams[i])
