# Your solution to Exercise 15

dd = int(input())
mm = int(input())
yyyy = int(input())

if dd == 31 and mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10:
   print (f"{1}.{mm + 1}.{yyyy}")
elif dd == 31 and mm == 12:
  print (f"{1}.{1}.{yyyy + 1}")
elif dd == 30 and mm == 4 or mm == 6 or mm == 9 or mm == 11:
  print (f"{1}.{mm + 1}.{yyyy}")
elif dd == 28 and mm == 2 and yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0 :
  print (f"{dd + 1}.{2}.{yyyy}")
elif dd == 29 and mm == 2 and yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0:
  print (f"{1}.{3}.{yyyy}")
else:
  print (f"{dd + 1}.{mm}.{yyyy}")
