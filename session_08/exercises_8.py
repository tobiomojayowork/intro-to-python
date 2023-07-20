# Session 8 Exercises


# All of these questions will use a set of pre-made files with data in. The files are in the text_files directory.
# In order to access the text files from this file, make sure you get into the text_files directory when using read/write.
# Ex: f = open("text_files/austen.txt", "r") OR f = open("text_files/register.txt", "w")


filedir = "text_files/"

## Section A
# 1. Read the file 'jabberwocky.txt' and print its content to the screen.

#f = open(filedir+"jabberwocky.txt", "r")
#print(f.read())

# 2. Read the file 'austen.txt' and print the amount of lines in the file.
# f = open(filedir+"austen.txt", "r")
# linecount = 0
# for l in f:
#    linecount+=1

# print(linecount)
# print(f.read())
    

# 3. Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file.
'''
f = open(filedir+"numbers.txt", "r")
total = 0
linecount = 0
for l in f:
    total+=int(l)
    linecount +=1

print("total number of numbers: " + str(linecount) + ", total is " + str(total))
'''
# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter their name and append this to a file called 'register.txt'.
'''
name = input("Enter your name to register: ")
f = open(filedir + "register.txt", "a")
f.write(name + "\n")
f.close()
'''



# 2. Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt'.
'''
feven = open(filedir + "even.txt", "a")
fnums = open(filedir + "numbers.txt", "r")

for num in fnums:
    if int(num) % 2 == 0:
        feven.write(num)

feven.close()
fnums.close()
'''

# 3. 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26. 
#    Work out what the secret message says.
'''
f = open(filedir+"secret.txt", "r")
alph = "abcdefghijklmnopqrstuvwxyz"
message = ""

for n in f:
    i = int(n) - 1
    message = message + alph[i]
    
f.close()
print(message)
'''


# 4. Benford’s law states that the leading digits in a collection of data are probably going to be small. 
#   For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). 
#   Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. 
#   Work out which of the files contains fake data.


def analyse_file(filenum):
    print("\n\nAnalysis for accounts " + str(filenum))
    f = open(filedir+ "accounts_" + str(filenum) + ".txt", "r")
    
    digitcount = {}

    for n in f:
        n = n.replace(".", "")
        n = n.replace("\n", "")
        for d in n:
            if d not in digitcount:
                digitcount[d] = 1
            else:
                digitcount[d] += 1
    
    #print(digitcount)
    total = 0
    for d in digitcount:
        total += digitcount[d]

    for d in digitcount:
        #print(d)
        print(d + ": " + str(
                total/digitcount[d]
                ) + "%")

    f.close()
    f = None 

analyse_file(1)
analyse_file(2)
analyse_file(3)