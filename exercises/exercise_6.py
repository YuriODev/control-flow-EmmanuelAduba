# Your solution to Exercise 6

x = 0
y = 0

O = (x, y)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Addition
A = x1 + y1
B = x2 + y2

# Division
# Gradient_A = (y1)/(x1)
# Gradient_B = (y2)/(x2)

# Floor Division
Afd = (x1 // y1)
Bfd = (x2 // y2)

if Afd == Bfd:
  print ("A and B are at the same distance from the origin.")
elif A > B:
  print ("A is further from the origin.")
elif A < B:
  print ("B is further from the origin.")

# NOT WORKING CODE

