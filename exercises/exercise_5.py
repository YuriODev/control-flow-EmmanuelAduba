# Your solution to Exercise 5

a = int(input())
b = int(input())
c = int(input())

x = ((-1)*(b)/2*a + (b**2 - 4*a*c))/(2*a)
y = ((-1)*(b)/2*a - (b**2 - 4*a*c))/(2*a)

if x == y:
  print ("One root:", x)
elif x != y:
  print ("Two roots:", x, y)
else:
  print ("No roots")

# NOT WORKING CODE

# ______________________________________________________________________________________________

# from math import sqrt

# def quadratic_formula(a, b, c):
#     discriminant = b**2 - 4*a*c
#     if discriminant < 0:
#         return "No real roots"
#     elif discriminant == 0:
#         root = -b / (2*a)
#         return root
#     else:
#         root1 = (-b + sqrt(discriminant)) / (2*a)
#         root2 = (-b - sqrt(discriminant)) / (2*a)
#         return (root1, root2)

