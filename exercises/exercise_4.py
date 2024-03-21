# Your solution to Exercise 4

grade = int(input())

if grade in range (1,13):
  if grade in range (1,4):
    print ("initial level.")
  elif grade in range (4,7):
    print ("average level.")
  elif grade in range (7,10):
    print ("sufficient level.")
  elif grade in range (10,13):
    print ("high level.")
else:
  print ("level is absent.")


