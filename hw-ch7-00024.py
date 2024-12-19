infile_boy = open("/content/BoyNames.txt","r")
infile_girl = open("/content/GirlNames.txt","r")

boy_names = []
girl_names = []

for line in infile_boy:
  boy_names.append(line.strip())

for line in infile_girl:
  girl_names.append(line.strip())

infile_boy.close()
infile_girl.close()

name = input("Enter 'boy', 'girl', or 'both':")


if name == "boy":
  pop_name = input(f"Enter a {name}'s name:")
  if pop_name in boy_names:
    print(f"{pop_name} was a popular boy's name between 2000 and 2009.")
  else:
    print(f"{pop_name} was not a popular boy's name between 2000 and 2009.")

elif name == "girl":
  pop_name = input(f"Enter a {name}'s name:")
  if pop_name in girl_names:
    print(f"{pop_name} was a popular girl's name between 2000 and 2009.")
  else:
    print(f"{pop_name} was not a popular girl's name between 2000 and 2009.")

elif name == "both":
  pop_boy_name = input("Enter a boy's name:")
  if pop_boy_name in boy_names:
    print(f"{pop_boy_name} was a popular boy's name between 2000 and 2009.")
  else:
    print(f"{pop_boy_name} was not a popular boy's name between 2000 and 2009.")
  
  pop_girl_name = input(f"Enter a girl's name:")
  if pop_girl_name in girl_names:
    print(f"{pop_girl_name} was a popular girl's name between 2000 and 2009.")
  else:
    print(f"{pop_girl_name} was not a popular girl's name between 2000 and 2009.")


