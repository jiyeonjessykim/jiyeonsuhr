list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [None] * (len(list1) + len(list2))
list3[::2] = list1
list3[1::2] = list2
print(list3)
