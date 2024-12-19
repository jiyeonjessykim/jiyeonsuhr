n = int(input("Enter any number:"))
factors = []

for x in range (2,n,1):
  if n % x == 0:
    factors.append(x)

factors.sort()

print(factors)
