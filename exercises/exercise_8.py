# Your solution to Exercise 8

integer = int(input("Enter a three digit integer: "))
digit = int(input("Enter a digit: "))

if digit == integer // 100:
  print ("True")
elif digit == integer // 10 % 10:
  print ("True")
elif digit == integer % 10:
  print ("True")
else:
  print ("False")
