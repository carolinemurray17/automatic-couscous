import random
from random import shuffle

#creating an empty team list
team = []

#gathering the number of team members and the members' names
n = int(input("How many team members? List their names."))

for i in range(0, n): 
    team_member = input()
    team.append(team_member) 
    # adding the team members

#randomizing and alphabetizing function
def order_generator(action):
    if action == "alphabetize":
        team.sort()
        print(team)
    elif action == "randomize":
        random.shuffle(team)
        print(team)
    else:
        print("That wasn't an option!")

#asking the user what they would like to do      
action = input("Would you like to alphabetize or randomize?")
#completing the requested action
order_generator(action)