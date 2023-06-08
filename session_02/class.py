myvar = 24.456000 
MYVAR = 0
my_complicated_name = "Babatiseunfunwa Oluwatobi Omojayowagbe"

#print(myvar)
print("My complicated name is " + str(len(my_complicated_name)) + " letters long")

firstnamestartindex = 6
firstnameendindex = 10

my_desired_firstname = my_complicated_name[firstnamestartindex:firstnameendindex]
my_desired_middlename = my_complicated_name[21:-13]
my_desired_surname = my_complicated_name[-12:-6]

print("The short form of my name is " 
      + my_desired_firstname + " "
      + my_desired_middlename + " " 
      + my_desired_surname
     )

# slicing [zero index to start: index to end (exclusive): number of characters to jump, it will ignore it if it is out of range]