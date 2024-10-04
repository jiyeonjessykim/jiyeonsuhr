#negative terminates
#sum of even integers

value = 1
even = 0

while value > 0:
    value = int(input())
    if value % 2 == 0 and value > 0:
        even += value

print(even)
