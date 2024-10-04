n = int(input("Enter a nonnegative integer:"))

total = 1

for n in range (1, n+1):
    if n >= 1:
        total *= n

print(total)


