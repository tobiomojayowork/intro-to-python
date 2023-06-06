#Python environments 
#https://code.visualstudio.com/docs/python/environments



# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
height = 9
width = 10 
area = width * height 

print("\n\nA1")
print("Retangle of Rectangle of width " 
      + str(width) + " and height " 
      + str(height) + " has an area of " 
      + str(area))


# 2. Write code that prints the length of the string, 'python'.

str_len = len("python")

print("\n\nA2")
print(str(str_len))



# 3. Print out the first and third letter of the word 'python'.

py_name = "python"

print("\n\nA3")
print(py_name[0])
print(py_name[2])




# 4. Ask the user to enter their name, and print out `Hello, <name>`.
print("\n\nA4")
your_name = input("What's your name? ")

print("Hello, " + your_name + "!")


# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
print("\n\nA5")
your_age = int(input("How old are you now? "))
your_age_in_15 = your_age + 15

print("You'll be " + str(your_age_in_15) + " in fifteen years from now!")


# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
print("\n\nA6")
print("Hello again, " + your_name 
      + ", you are currently " + str(your_age) 
      + " years old. " 
      + "But fifteen years time you will be " + str(your_age_in_15))


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
print("\n\nA7")
hometown = input("What is your home town?  ")
print(hometown.upper())


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
print("\n\nA8")
favcolour = input("What's your favourite colour?  ")
print(str(len(favcolour)))



# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
print("\n\nA9")
the_month = input("What month is it?  ")
the_weather = input("What is the weather? You can say things like `Rainy`, or `Windy`, or `Hot` or `Cold`, ...  ")

print("It is " + the_month + " and it is " + the_weather + " today.")





# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
print("\n\nA10")
the_month = input("What month is it?   ")
t0 = int(input("Enter a temperature in °C  "))
t1 = int(input("Enter a temperature in °C  "))
t2 = int(input("Enter a temperature in °C  "))
t3 = int(input("Enter a temperature in °C  "))
t4 = int(input("Enter a temperature in °C  "))

ta = (t0+t1+t2+t3+t4)/5

print("It is " + the_month + " and the average temperature is " + str(ta) + "°C.")



# 11. Print out the above sentence but make the month upper case.
print("\n\nA11")
print("It is " + the_month.upper() + " and the average temperature is " + str(ta) + "°C.")


# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
animals = "Dog Puppy Cat Kitten Chicken Chick"



print("\n\nA12")
print("\t"+animals[0:3])
print("\t"+animals[4:9])
print("\t"+animals[10:13])
print("\t"+animals[14:20])
print("\t"+animals[21:28])
print("\t"+animals[29:])


# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
print("\n\nA13")
your_name = input("What's your name? ")
your_age = int(input("Enter a number from 0 to " + str(len(your_name)-1) + " "))
print(your_name[your_age])

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".



my_complicated_name = "Babatiseunfunwa Oluwatobi Omojayowagbe"
