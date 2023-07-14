myplace = {
    "town": "Ikeja",
    "region": "Lagos",
    "country": "Nigeria"
}


print(myplace)

for key in myplace:
    print(str(key) + " = " + str(myplace[key]))

print(myplace.get("town"))
print(myplace["town"])

myplace["town"] = "Agege"

for key in myplace:
    print(str(key) + " = " + str(myplace[key]))



