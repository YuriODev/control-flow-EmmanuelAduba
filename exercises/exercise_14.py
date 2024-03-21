# Your solution to Exercise 14

integer = int(input("Enter a four digit integer: "))

if integer // 1000 == integer % 10 and integer // 100 % 10 == integer // 10 % 10:
  print ("True")
else:
  print ("False")
