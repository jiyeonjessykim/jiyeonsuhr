golf = open("golf.txt", "w")

number = int(input("Enter number of players:"))
player_number = 0

for i in range(number):
  player_number += 1
  player = str(input(f"Enter name of player number {player_number}:"))
  score = int(input(f"Enter score of player number {player_number}:"))
  golf.write(f"{player}\n{score}\n")


golf.close()
  
