age = int(input())
choice = input()

if age <= 21 and choice == "S":
    print("vegetable juice")

elif age <= 21 and choice == "T":
    print("cranberry juice")

elif age <= 21 and choice == "B":
    print("soda")

elif age > 21 and choice == "S":
    print("cabernet")

elif age > 21 and choice == "T":
    print("chardonnay")

elif age > 21 and choice == "B":
    print("IPA")

else:
    print("invalid menu selection")


