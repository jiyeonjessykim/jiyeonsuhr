#full-time $8000
#increase by 3 percent for the next 5 years

tuition = 8000

for year in range (1,6):
    if year == 1:
            tuition = tuition * 1.03
            print(f"In {year} year, the tuition will be ${tuition}.")
    else:
        tuition = tuition * 1.03
        print(f"In {year} years, the tuition will be ${tuition}.")
