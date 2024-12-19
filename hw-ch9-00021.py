course_info = {}
course_info["CS101"] = [3004, "Haynes", "8:00AM"]
course_info["CS102"] = [4501, "Alvarado", "9:00AM"]
course_info["CS103"] = [6755, "Rich", "10:00AM"]
course_info["NT110"] = [1244, "Burke", "11:00AM"]
course_info["CM241"] = [1411, "Lee", "1:00PM"]

find = input("Enter a class name:")

for k,v in course_info.items():
  if find == k:
    print(f"Class: {k}\nRoom: {course_info[k][0]}\nInstructor: {course_info[k][1]}\nTime: {course_info[k][2]}")\
    


