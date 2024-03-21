# Your solution to Exercise 16

dd = int(input())
mm = int(input())
yyyy = int(input())

if dd == 1 and mm == 1:
  print (f"{31}.{12}.{yyyy - 1}")
elif dd == 1 and mm == 2 or mm == 4 or mm == 5 or mm == 6 or mm == 7 or mm == 8 or mm == 9 or mm == 10 or mm == 11 or mm == 12:
  print (f"{31}.{mm - 1}.{yyyy}")
elif dd == 1 and mm == 3 and yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0 :
  print (f"{29}.{2}.{yyyy}")
elif dd == 1 and mm == 3 and yyyy % 4 != 0:
  print (f"{28}.{2}.{yyyy}")
else:
  print (f"{dd - 1}.{mm}.{yyyy}")
