mytowns = {
  "Lagos", 
  "Ibadan",
  "Ijebu",
  "Akure",
  "Ikeja",
  "Ilorin", 
  "Lagos"
}
print(mytowns)

print("\nSet: cannot be sorted...")
print("\nSet: DOES NOT SUPPORT INDEXING!!!")

print("\nSet: can be changed: by adding and removing only apparently")

mytowns.remove("Ikeja")

print(mytowns)

mytowns.add("Badagry")

print(mytowns)

mytowns.discard("Ibadan")

print(mytowns)

mytowns.pop()

print(mytowns)


print("\n\nSets: can be iterated at least!...")
for item in mytowns:
  print(item)
  