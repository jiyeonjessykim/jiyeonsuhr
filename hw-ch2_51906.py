S = "S"
T = "T"
B = "B"

age = int(input( ))
choice = input()



if choice != "S" and choice != "T" and choice != "B":
    print("invalid menu selection")

if age <= 21 and choice == "S":
    print("vegetable juice")

if  age <= 21 and choice == "T":
    print = ("cranberry juice")

if age <= 21 and choice == "B":
    print("soda")

if  age > 21 and choice == "S":
    print("cabernet")

if age > 21 and choice == "T":
    print("chardonnay")

if age > 21 and choice == "B":
    print("IPA")



