
age = int(input( ))
choice = input()

if choice == "S":
    if age <= 21:
        print("vegetable juice")
    else:
        print("cabernet")

elif choice == "T":
    if age <= 21:
        print("cranberry juice")
    else:
        print("chardonnay")

elif choice == "B":
    if age <= 21:
        print("soda")
    else:
        print("IPA")

else:
    print("invalid menu selection")
      
