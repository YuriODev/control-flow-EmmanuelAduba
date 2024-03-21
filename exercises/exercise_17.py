# Your solution to Exercise 17

integer = int(input("Enter a six digit integer: "))

sumA = integer // 100000 + integer // 10000 % 10 + integer // 1000 % 10
sumB = integer // 100 % 10 + integer // 10 % 10 + integer % 10

if sumA == sumB:
  print ("Happy")
else:
  print ("Ordinary")
