age = int(input())

if age < 2:
    print("ineligible")

elif age == 2:
    print("toddler")

elif 3 <= age <= 5:
    print("early childhood")

elif 6 <= age <= 7:
    print("young reader")

elif 8 <= age <= 10:
    print("elementary")

elif age == 11 or age == 12:
    print("middle")

elif age == 13:
    print("impossible")

elif 14 <= age <= 16:
    print("high school")

elif 17 <= age <= 18:
    print("scholar")

else:
    if age > 18:
        print("ineligible")

