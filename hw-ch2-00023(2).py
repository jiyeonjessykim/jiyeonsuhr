males = int(input("Enter number of males:"))
females = int(input("Enter number of females:"))

percent_males = males / (males + females)
percent_females = females / (males + females)

percent_males = format(percent_males, ".0%")
percent_females = format(percent_females, ".0%")

print(percent_males)
print(percent_females)


                    
