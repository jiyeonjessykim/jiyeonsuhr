numbers = open('numbers.txt', 'r')
lines = numbers.readlines()

runsum = 0
max = 0
for line in lines:
  line = int(line)
  if line > max:
    max = line
    runsum += line

print(runsum)

numbers.close()
