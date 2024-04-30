#======= Question 1 =======

# Task 1: Code Correction

# Buggy Code

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2: expand options for cave

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You were eaten by a grue!")

# Task 3: add pass statements for invalid input

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You were eaten by a grue!")
    else:
        pass
else:
    pass

#======= Question 2 =======

# Task 1: Code Correction

# Buggy Code

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(f"Have your event in a {venue}.")

# Task 2: make additional recommendations

screen = "projector" if attendees > 4 else "laptop"
sound = "an audio system" if attendees > 12 else "shouting"
print(f"You can present slides on a {screen} and communicate through {sound}")

# Task 3: recommend catering

is_vegetarian = input("Would you like vegetarian food (yes/no)? ")
caterer = "Veggie Delight Caterers" if is_vegetarian == "yes" else "Gourmet Meals Caterers"
print(f"Then let's order from {caterer}.")