#land air water
#terminates when "xxxxx"
#after the loop, "land:" number, "air:" number, "water:" number


user_input = str

land_count = 0
air_count = 0
water_count = 0


while user_input != "xxxxx":
    user_input = input()
    if user_input == "land":
        land_count += 1
    elif user_input == "air":
        air_count += 1
    elif user_input == "water":
        water_count += 1

print(f"land:{land_count}")
print(f"air:{air_count}")
print(f"water:{water_count}")
        
