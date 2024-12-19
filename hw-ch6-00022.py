number = open("/num.txt","r")

lines = number.readlines()

total = 0

for line in lines:
	line = int(line)
	total += line

print(total)
	
number.close()
