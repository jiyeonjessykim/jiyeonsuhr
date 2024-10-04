males = int(input("Enter number of males:"))
females = int(input("Enter number of females:"))

percent_males = int(males / (males + females) * 100)
percent_females = int(females / (males + females) * 100)

print(f"Percent males: {percent_males}%")
print(f"Percent females: {percent_females}%")
