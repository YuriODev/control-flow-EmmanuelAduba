# Your solution to Exercise 9

integer = int(input("Enter a three digit integer: "))

sum = integer // 100 + integer % 10

if sum > integer // 10 % 10:
  print (">")
elif sum == integer // 10 % 10:
  print ("=")
else:
  print ("<")
