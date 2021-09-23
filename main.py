stu_gra = {"Harry": 66, "Joe": 77, "Tim": 88}

for grades in stu_gra.items():
  print(grades)

for grades in stu_gra.keys():
  print(grades)

for grades in stu_gra.values():
  print(grades)

user_name = " "

while user_name != "Art":
  user_name = input("Enter your name:")

username = " "

while True:
  username = input("Enter username: ")
  if username == "Art":
    break
  else:
    continue