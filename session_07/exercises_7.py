# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
def my_name_is1():
    print("My name is Seun T")



# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
def my_name_is2(name):
    print("My name is " + name)


# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
names = ["Alice", "Bob", "Charlie", "Seun T"]

for name in names:
    my_name_is2(name)


# 4. Write a function that prints the area of two passed in parameters.



# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
def print_list(mylist):
    for item in mylist:
        print("item: " + item)

print_list(["bread", "eggs", "potatoes", "fish and chips"])


# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".

def age_test(age):
    if age <= 0:
        print("You're not born yet!")
    elif age < 11:
        print("You're too young to go to this school")
    elif age >= 11 and age < 16:
        print("You can can come to this school")
    else:
        print("You're too old for school")

age_test(2)
age_test(0)
age_test(11)
age_test(12)
age_test(14)
age_test(22)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
def is_odd(num):
    return num % 2 != 0

print(is_odd(2))
print(is_odd(33))
print(is_odd(44))


# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.
def my_reverse(word):
    reversed = []
    for letter in word:
        reversed.insert(0, letter)
    
    reversed_str = ""

    for letter in reversed:
        reversed_str += letter

    return reversed_str



print(my_reverse("this is something else"))


# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```

def stars_tree(num):
    stars_str = ""
    for n in range(num):
        stars_str += "*"
    
    print(stars_str)

    if num != 0:
        stars_tree(num-1)


stars_tree(5)


# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".
def padlock(code):
    lockcode = 1234

    if code == lockcode:
        return "Locked"
    return "Unlocked"


#lock_state = padlock(input("Enter passcode: "))
#print(lock_state)
    
lock_state = padlock("1234")
print(lock_state)
    
lock_state = padlock(None)
print(lock_state)
    
lock_state = padlock(0)
print(lock_state)
    
lock_state = padlock(34556)
print(lock_state)
    
lock_state = padlock(1234)
print(lock_state)
    



# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def multiple_sum(figure):
    sum = 0
    for n in range(1, figure+1):
        #print(n)

        if n % 3 == 0:
            sum += n

        if n % 5 == 0:
            sum += n
    
    return sum



#print(multiple_sum(12))
#print(multiple_sum(5))
print(multiple_sum(30))
#print(multiple_sum(40))

# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.
def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    
    return True


def print_is_prime(number):
    print("Is " + str(number) + " a prime number? " + str(is_prime(number)).upper())
    
print_is_prime(44)
print_is_prime(2)
print_is_prime(1)
print_is_prime(7)
print_is_prime(8)
print_is_prime(9)
print_is_prime(11)
print_is_prime(13)
print_is_prime(55)

# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.
def is_pallindr(string):
    string = string.replace(" ", "").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("’", "").lower()

    reverse_string = ""
    for l in reversed(string): 
        reverse_string += l

    return (string == reverse_string)

print(is_pallindr("this is a sentence "))
print(is_pallindr("Red roses run no risk, sir, on Nurse’s order"))
print(is_pallindr("Now, sir, a war is won!"))
print(is_pallindr("UFO tofu"))
print(is_pallindr("Step on no pets!"))
print(is_pallindr("Yo, Banana Boy!"))
print(is_pallindr("rotator"))
print(is_pallindr("Dennis and Edna sinned."))
print(is_pallindr("Borrow or rob?"))
print(is_pallindr("mallam"))

# https://www.dictionary.com/e/palindromic-word/



# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
