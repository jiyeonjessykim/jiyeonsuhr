infile = open("phonebook.in", "r")

lines = infile.readlines()
name = []
email = []

for line in lines:
  line = line.strip()
  if "@" not in line:
    name.append(line)
  else:
    email.append(line)
    
infile.close()

phonebook = {}
for k,v in zip(name, email):
  phonebook[k] = v

while True:
  number = input(f"Enter\n1. look up an email address\n2. add a new name and email address\n3. change an email address\n4. delete a name and email address\n5. save address book and exit:")

  if number == "1":
    one = input("Enter name:")
    if one in phonebook.keys():
      print(phonebook[one])
    else:
      print("Sorry, no contact exists under that name.")

  elif number == "2":
    two_name = input("Enter new name:")
    two_email = input("Enter new email address:")
    phonebook[two_name] = two_email

  elif number == "3":
    three_name = input("Enter name:")
    three_email = input("Enter new email address:")
    if three_name in phonebook.keys():
      phonebook[three_name] = three_email

  elif number == "4":
    four = input("Enter name:")
    if four in phonebook.keys():
      del phonebook[four]


  elif number == "5":
    sorted_phonebook = dict(sorted(phonebook.items())) 
    outfile = open("phonebook.out", "w")
    for name, email in sorted_phonebook.items():
      outfile.write(f"{name}\n{email}\n")
    outfile.close()
    break 
