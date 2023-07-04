import random
from math import floor
'''
# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
print(random.random())

print("\n\nA1: random numbers")

count = 10

while count != 0:
  print(str(count) + ". " + str(random.randint(1, 10000)))
  count -=1


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
print("\n\nA3: capture the lucky number")
lucky_number = 99

while lucky_number != 7:
  lucky_number = int(input("Please enter a number between 1 and 10 and find out if it is lucky...: "))

print("WOW! You entered the lucky number 7!!!")





# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.

from math import ceil

width = int(input("\n\nA3\n\nEnter the width in CM: "))
height = int(input("Enter the height in CM: "))

area = ceil(((width * height)/100))

print("The area is: " + str(area) + " metres")

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".

count = 0
password = None

while count != 3:
  count +=1
  password = input("\n\nA4:\nEnter your password: ")
  if(password != "qwerty123"):
    print("Invalid password")
    



# 5. Add up all the numbers from 1 to 500 and print the answer.
count = 500
total = 0

while count != 0:
  total += count
  count -=1
  
print("\n\nA5: The total is: " + str(total))


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
numlist = []

for n in range(10):
  num = int(input("\n\nA6: Enter a number between 1 and 100 (one must be 99): "))
  numlist.append(num)

if 99 in numlist:
  print("The number 99 is at " + str(numlist.index(99)))
else:
  print("You didn't enter the number 99!")


# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
print("\n\nA7: Multiplication table x 18")
count = 1 

for n in range(1, 16):
  print(str(n) + " x 18 = " + str(n*18))



# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
print("\n\nA8: RAnge")
for n in range(1, 101):
  print(n)

'''
# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

print("\n\nA9: school grades (v2)")

schl = [["", ""], ["", ""], ["", ""]]

for cls in schl:
  cls[0] = input("enter the lesson: ")
  mark = int(input("enter your marks for " + cls[0].upper() + " lesson: "))
  while mark != 0:
    if mark >= 80:
      cls[1] = "A"
      break
    elif mark >= 60 and mark < 80:
      cls[1] = "B"
      break
    elif mark >= 50 and mark < 60:
      cls[1] = "C"
      break
    elif mark >= 45 and mark < 50:
      cls[1] = "D"
      break
    elif mark >= 25 and mark < 45:
      cls[1] = "E"
      break
    elif mark < 25:
      cls[1] = "F (go see the teacher)"
      break
    mark -=1

print("\n\nREPORT:\n")

for cls in schl:
  print("lesson " + cls[0].upper() + " grade: " + cls[1])



# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name



# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
