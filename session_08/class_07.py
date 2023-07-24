f = open("odd.txt", "w")

for x in open("numbers.txt"): 
    x = int(x) 
    if x % 2 == 1: 
        f.write(str(x) + "\n")

f.close()