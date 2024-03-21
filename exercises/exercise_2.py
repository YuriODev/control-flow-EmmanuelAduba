# Your solution to Exercise 2

person = int(input())

if person <= 1:
  print ("You are an infant.")
elif person > 1 and person < 13:
  print ("You are a child.")
elif person > 13 and person < 20:
  print ("You are a teenager.")
elif person > 20:
  print ("You are an adult.")
