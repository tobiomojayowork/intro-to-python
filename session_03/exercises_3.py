# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
print("A1:")
username = input("Enter your name: ")

if username == "Tolu":
  print("You are most welcome, Olutolu!")


# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
print("\n\nA2:")
username = input("Enter your name again: ")

if username != "Tolu":
  print("Hmm... you're not Tolulope. You are " + username + "! ")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
print("\n\nA3:")
password = input("Please enter your password: ")

if password == "qwerty123": 
  print("Successfully logged in")
else:
  print("Password incorrect, you are not logged in")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
print("\n\nA4:")

numev = int(input("Please enter a number: "))

if numev % 2 == 0: 
  print("EVEN NUMBER!")
else: 
  print("The number you provided, " + str(numev) + " is ODD")




# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
print("\n\nA5:")
num1 = int(input("Please provide a number: "))
num2 = int(input("Please provide another number: "))

if (num1+num2) > 21:
  print("Bust")
else: 
  print("Safe")


# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
print("\n\nA6:")
num1 = int(input("Please provide a length: "))
num2 = int(input("Please provide a width: "))

if num1 == num2:
  print("Its a SQUARE!")
else:
  print("...nah! It's something else but a square :(")



# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
print("\n\nA7:")
currsal = float(input("Enter your current salary: "))
numyrs = int(input("Enter your years of service: "))

print("Your salary is: " + str(currsal) + " and . . .  ")

if numyrs > 3:
  print("\tyour bonus is: " +str(currsal*0.1))
else:
  print("\t aww! you have no bonus!")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
print("\n\nA8:")
num1 = int(input("please enter a number: "))

if num1 > 0:
  print(str(num1 ** 3))
else:
  print(str(num2/2))

# indentation needs to be consistent: it can be one or two or three or four spaces
# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
print("\n\n\nB1:")
username = input("Enter your name: ")

if username == "Tolu":
  print("Hello Tolulope")
elif username == "Bayo":
  print("OK... you're not Olutolu. I am Olutolu!!!")
else: 
  print("Ah.... you must be Seun.")



# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
print("\n\nB2:")
numyrs = int(input("Enter your age: "))
if numyrs == 0:
  print("You're not born yet!")
elif numyrs < 11:
  print("You're too young to go to this school")
elif numyrs >= 11 and numyrs <= 16:
  print("You can can come to this school")
elif numyrs > 16:
  print("You're too old for school")



# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
print("\n\nB3:")
themonth = input("Enter a month of the year to find out the season: ").lower()

theseason = ""

if themonth == "december" or "january" or "february":
  theseason = "Winter"
elif themonth == "march" or "april" or "may":
  theseason = "Spring"
elif themonth == "june" or "july" or "august":
  theseason = "Summer"
elif themonth == "september" or "october" or "november":
  theseason = "Autum"

if len(theseason) > 0: 
  print("The month of " + themonth + " is " + theseason + "!")
else:
  print("I don't know")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.



# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.



# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.



# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.



# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
