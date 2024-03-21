# Your solution to Exercise 13

integer = int(input("Enter a four digit integer: "))

if integer // 1000 == integer // 100 % 10 or integer // 1000 == integer // 10 % 10 or integer // 1000 == integer % 10 or integer // 100 % 10 == integer // 10 % 10 or integer // 100 % 10 == integer % 10 or integer // 10 % 10 == integer % 10:
  print ("False")
else:
  print ("True")

