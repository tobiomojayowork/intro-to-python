print("The oddity of range\n\n\n")
"""
Is this a comment? YES!!! A COMMENT BLOCK!!! 
...with a space, it seems
"""

#you can't just provide the start or even the start and end... They are zero based.
print("\n\nTRY zero based (10):")
for n in range(10):
  print(n)

#so to logically print a range of numbers, either add 1 to the end OR use n+1 for each number (the latter doesn't make sense!)
print("\n\nzero based conundrum. try (1, 11):")
for n in range(1, 11):
  print(n)

print("\n\n. . .or this (10), n+1 in loop:")
for n in range(10):
  print(n+1)

print("\n\nTRUE/FALSE evaluations")
if not (""):
  print("empty string is FALSE")
  
if not (0):
  print("0 is FALSE")
  
if not (None):
  print("None is FALSE")

nonevar = None
if not (nonevar):
  print("a None var string is FALSE")

deletedvar = 1000 
if (deletedvar):
  print("assigned var is true")

deletedvar = None
if not (deletedvar):
  print("var set to None is FALSE")
  
del(deletedvar)
#a del(eted) var is ...removed and is unassigned


print("\n\nTRY 1:")
total = 0
for num in range(1, 4):
  total = total + num
print("The total is: " + str(total))

print("\n\nTRY 2:")
for x in range(1, 10, 2): 
  print(x)
