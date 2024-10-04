weight_of_package = float(input("Enter the weight of the package: "))

shipping_charge = 0.0

if weight_of_package <= 2:
    shipping_charge = 1.5

elif 2 < weight_of_package <= 6:
    shipping_charge = 3.00

elif 6 < weight_of_package <= 10:
    shipping_charge = 4.00

else:
    if 10 < weight_of_package:
            shipping_charge = 4.75


total = weight_of_package * shipping_charge

print("Shipping charge:", format(shipping_charge,'.2f'))
print("Total cost:",format(total,'.2f'))
