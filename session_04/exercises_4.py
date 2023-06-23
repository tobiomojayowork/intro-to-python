# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
print("A1:")
my_fruit = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(my_fruit)

# 2. Add "Grapes" to the list and print the list.
print("\n\nA2: insert and append!")
my_fruit.insert(5, "Prunes")
my_fruit.append("Grapes")
print(my_fruit)

# 3. Change "Pears" to "Strawberries" and print the list.
print("\n\nA3:")
my_fruit[2] = "Strawberries"
print(my_fruit)

# 4. Remove "Apples" from the list and print the list.
print("\n\nA4:")
del(my_fruit[0])
print(my_fruit)

# 5. Print out the current length of the list.
print("\n\nA5:")
print(len(my_fruit))


# 6. Order the list alphabetically.
print("\n\nA6:")
my_fruit.sort()
print(my_fruit)



# 7. Print out the list again.




# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
print("\n\nB1:")
for fruit in my_fruit:
    print("fruit: " + fruit)


# 2. Print the numbers 1 to 100 (including the number 100).
print("\n\nB2:")
for n in range(1, 101):
  print(n)





# 3. Print all odd numbers from 1 to 100.
print("\n\nB3:")
for n in range(1, 101):
  if n % 2:
    print(n)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
print("\n\nB4: years olympics were held since")
olympics_not_held = [1916, 1940, 1944, 2020]
for year in range(1896, 2023):
  if not year % 4 and year not in olympics_not_held:
    print(year)


# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
print("\n\nB5: even, odd count")
myrands = [23, 99, 345, 89, 1129, 55, 66, 452, 92, 1532]
oddcount = 0
evencount = 0

for n in myrands:
  if n %2:
    evencount +=1
  else:
    oddcount +=1

print("Odd numbers: " + str(oddcount) + "\nEven numbers: " + str(evencount))



# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
print("\n\nB6: my Naija names...")
mynames = ["Joke", "Ade", "Olu", "Ola", "Seun"]

for name in mynames:
  print("Hello " + name)


# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
#wow! so a string variable is simply a list of string characters that can be ... listed!
print("\n\nB7: letter listing")
somword = "supercalifragilisticexpialidocious"

for letter in somword:
  print(letter)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
#gets Killed!
#you can't loop through and alter a list at the same time
print("\n\nB8: square listing")
mynumlist = [4, 88, 2, 3, 99]
mynumlist2 = []

for num in mynumlist:
  mynumlist2.append(num**2)

for num in mynumlist2:
  mynumlist.append(num)
  
print(mynumlist)


# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
print("\n\nB9: append title")
title = "Dr"

for name in mynames:
  mynames[mynames.index(name)] = title + " " + name

print(mynames)


# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

print("\n\nB10:")
for n in range(1, 101):
  if  not n % 3 and not n % 5:
    print("FizzBuzz") 
  elif not n % 3:
    print("FIZZ")
  elif not n % 5:
    print("buzz")
  else:
    print(n)
    
#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
