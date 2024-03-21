# Your solution to Exercise 3

number = int(input())

if number in range (0,37):
  if number == 0:
    print ("Green")
  elif number in range (1,11):
    if number % 2 == 0:
      print ("Black")
    else:
      print ("Red")
  elif number in range (11,19):
    if number % 2 == 0:
      print ("Red")
    else:
      print ("Black")
  elif number in range (19,29):
    if number % 2 == 0:
      print ("Black")
    else:
      print ("Red")
  elif number in range (29,37):
    if number % 2 == 0:
      print ("Red")
    else:
      print ("Black")
else:
  print ("The bet will not play!")
