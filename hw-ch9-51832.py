election_results = {"John":20, "Jessy":356, "Elliot":93}

x = 0

for k, v in election_results.items():
  if v > x:
    x = v
    winner = k

print(winner)
