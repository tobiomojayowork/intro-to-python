#comments 
'''
multiline comments
'''

"""
multiline comments 
"""

import datetime


myvar = 1 
print(type(myvar))

myvar = "Blah"
print(type(myvar))

myvar = datetime.date.today()
print(type(myvar))

myvar = 23.4545
print(type(myvar))

myvar = 23j
print(type(myvar))

MYVAR = "variable names are case sensitive!"
print(type(MYVAR))

#multiword variable names can be camelCase, PascalCase or snake_case

a, b, c, d, e = "apple", 0.234, {"Something", "in", "here"}, 100334, 45555j

print("a = " + a +  
       " b = " + str(b) + 
       " c = " + str(c) + 
       " d = " + str(d) + 
       " e = " + str(e) 
       )

#unpack a collection - any collection! 
f, g, h = c
print("\n\nunpacking c.... f = " + f +  
       " g = " + g + 
       " h = " + h )


#output multiple variables even if they're different types!
print(a, b, d, e)

#global keyword assigns a variabl to teh global scope 
# # and you can change the scope of a vaiable using this keyword!
global myg 

#other variable types 

#complex
myc = 234.5j

#frozenset ... does this just have to be a set??? 
myfs = frozenset(["something", "in", "here"]) 


mybytes = b"this is a byte type"

mybytearray = bytearray(20)

mymemoryview = memoryview(bytes(10))

myfloat1 = 2e3
print(myfloat1)
print(type(myfloat1))