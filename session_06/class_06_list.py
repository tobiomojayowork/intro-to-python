mytowns = [
  "Lagos", 
  "Ibadan",
  "Ijebu",
  "Akure",
  "Ikeja",
  "Ilorin"
]

print(mytowns)

print("\n\nList: sort...")
mytowns.sort()

print(mytowns)


print("\n\nList: changeable...")
mytowns[4] = "Lekki"

print(mytowns)


print("\n\nList: Duplicates allowed...")
mytowns.append("Lagos")

print(mytowns)