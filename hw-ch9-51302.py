d = {1:2, 3:4, 5:6, 7:8}
lst = [1,7]

for x in lst:
  if x in d:
    del d[x]

print(d)
