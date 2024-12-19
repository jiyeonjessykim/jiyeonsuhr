
try:
  per_student = budget / (num_boys + num_girls)
  print(per_student)

except ZeroDivisionError:
  print("unavailable")
