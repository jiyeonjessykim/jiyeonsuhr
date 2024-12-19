ratio = int(input("Enter ratio: "))

n = int(input("Enter n: "))

value = 1

geom_prog = []

while value <= n:
    geom_prog.append(value)
    value *= ratio

print(geom_prog)
