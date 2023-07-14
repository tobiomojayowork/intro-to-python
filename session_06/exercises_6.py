# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".
print("\n\nA1: dictionary")
d = {"Type": "Bramley", "Price": 0.39, "Colour": "Green"}
print(d)

# 2. Add the best before date to the dictionary - print the dictionary.
print("\n\nA2: dictionary with bbd")
import datetime 
bbd = datetime.date.today().isoformat()

d["BestBeforeDate"] = bbd

print(d)


# 3. Change the price to 0.41 - print the dictionary.
print("\n\nA3: dictionary: change price")
d["Price"] = 0.41
print(d)


# 4. Set the apple to be on offer using a Boolean - print the dictionary.
print("\n\nA1: dictionary with apple on offer")
d["OnOffer"] = True
print(d)


# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.
print("\n\nA1: dictionary - remove offer")
del(d["OnOffer"])
print(d)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.

print("\n\nB1\n")
names = []
name = "start"
age = 0

while len(name) != 0:
    name = input("Enter your name: ")
    ageinput = input("Enter your age: ")

    if len(ageinput) != 0:
        age = int(ageinput)

    if len(name) > 0 and age > 0:
        names.append({"name": name, "age": age})

for n in names:
    print("\t" + n["name"] + ", " + str(n["age"]))






# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).

print("\n\nB2: restaurant menu\n\n")

menu = []

menu.insert(0, {
    "name": "fish stew",
    "price": 20.34
})

menu.append({
    "name": "bread and eggs",
    "price": 11.99
})

menu.insert(0, {
    "name": "avocado salad",
    "price": 8.20,
    "vegetarian": True
})

menu.append({
    "name": "oats with almond milk",
    "price": 7.454,
    "vegetarian": True
})

menu.append({
    "name": "sunday pork roast",
    "price": 28.54,
    "vegetarian": False
})

print("full menu:\n")

for menuitem in menu:
    for key in menuitem:
        print(str(key) + ": " + str(menuitem[key]))
    print("`\n")

print("\n\nvegetarian menu:\n")

for menuitem in menu:
    if "vegetarian" in menuitem and menuitem["vegetarian"]:
        print(menuitem["name"])





# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.

import random  

print("\n\nB3: the beetle game\n")

beetlebodyparts = (
    {
        "name": "body", 
        "count": 1
    },
    {
        "name": "head", 
        "count": 1, 
        "req": "body"
    },
    {
        "name": "leg", 
        "count": 6, 
        "req": "body"
    },
    {
        "name": "antenna", 
        "count": 2, 
        "req": "head"
    },
    {
        "name": "eye", 
        "count": 2, 
        "req": "head"
    },
    {
        "name": "mouth", 
        "count": 1, 
        "req": "head"
    }
)

totalpartcount = 0 

for part in beetlebodyparts:
    totalpartcount += part["count"]


beetle = []
roll = True

while roll and len(beetle) != totalpartcount:
    roll = (input("\n\nRoll the dice to play? (enter Y or N): ").upper() == "Y")

    if roll:
        dienum          = random.randint(0, 5)
        selectedpart    = beetlebodyparts[dienum]

        maxallowed      = selectedpart["count"]
        selectedpartname = selectedpart["name"].upper()
        prereqpart      = None

        if "req" in selectedpart:
            prereqpart = selectedpart["req"].upper()

        print("\ndice rolled to " + str(dienum+1) + "! you got " + selectedpartname)

        if beetle.count(selectedpartname) >= maxallowed:
            print("\t... but you've already got " + str(maxallowed) + " " + selectedpartname)

        elif prereqpart and prereqpart not in beetle:
            print("\t... but you need " + prereqpart + " to add a " + selectedpartname)
            
        else:
            beetle.append(selectedpartname)

if len(beetle) == totalpartcount: 
    print("\nEND OF GAME\nYOU WON! YOU BUILT THE BEETLE!!!!")

elif len(beetle) > 0:
    print("\nEND OF GAME\nBEETLE NOT COMPLETED!")
    print("\tyou got: ")

    for part in beetle:
        print("\t\t" + part.upper())

else:
    print(" :( you didn't play. exiting game")

