cable = input("Enter cable ('l', 'u', or 'h'):")
quantity = int(input("Enter quantity:"))

cost = float


if cable == "l":
    if 1 <= quantity <= 9:
        cost = 3.99
    elif quantity >= 10:
        cost = 3.26

elif cable == "u":
    if 1 <= quantity <= 9:
        cost = 2.99
    elif quantity >= 10:
        cost = 2.41

elif cable == "h":
    if 1 <= quantity <= 9:
        cost = 6.99
    elif quantity >= 10:
        cost = 5.51

else:
    cost = 0



subtotal = cost*quantity

shipping = 5.00


if subtotal >= 25.00 or subtotal == 0:
    shipping = 0

total = subtotal + shipping

print("Cost per cable:", format(cost,".2f"))
print("Subtotal:", format(subtotal,".2f"))
print("Shipping:", format(shipping,".2f"))
print("Total:",  format(total,".2f"))

    
