# Your solution to Exercise 18

remeber = input("Do you remeber the person's name? (yes/no)")
if remeber == "yes" or remeber == "Yes" or remeber == "YES":
  ex = input("Is it an ex? (yes/no)") 
  if ex == "yes" or ex == "Yes" or ex == "YES":
    drunk = input("Are you drunk? (yes/no)")
    if drunk == "yes" or drunk == "Yes" or drunk == "YES":
      rekindle = input("Do you want to rekindle and/or give 'em what for? (yes/no)")
      if rekindle == "yes" or rekindle == "Yes" or rekindle == "YES":
        print ("Say hi.")
      elif rekindle == "no" or rekindle == "No" or rekindle == "NO":
        print ("Don't say hi.")
    elif drunk == "no" or drunk == "No" or drunk == "NO":
      drunk = input("Are you in a convertible with Brad Pitt and/or Rihanna? (yes/no)")
      if drunk == "yes" or drunk == "Yes" or drunk == "YES":
        print ("Say hi.")
      elif drunk == "no" or drunk == "No" or drunk == "NO":
        print ("Don't say hi.")
  elif ex == "no" or ex == "No" or ex == "NO":
    ex = input("A friend's ex? (yes/no)")
    if ex == "yes" or ex == "Yes" or ex == "YES":
      print ("Don't say hi.")
    elif ex == "no" or ex == "No" or ex == "NO":
      ex = input("A enemy or frenemy? (yes/no)")
      if ex == "yes" or ex == "Yes" or ex == "YES":
        ex = input("Are you in a convertible with Brad Pitt and/or Rihanna? (yes/no)")
        if ex == "yes" or ex == "Yes" or ex == "YES":
          print ("Say hi.")
        elif ex == "no" or ex == "No" or ex == "NO":
          print ("Don't say hi.")
      elif ex == "no" or ex == "No" or ex == "NO":
        ex = input("Are you robbing a bank? (yes/no)")
        if ex == "yes" or ex == "Yes" or ex == "YES":
          print ("Don't say hi.")
        elif ex == "no" or ex == "No" or ex == "NO":
          ex = input("Are you in a bathrobe? (yes/no)")
          if ex == "yes" or ex == "Yes" or ex == "YES":
            print ("Dont say hi.")
          elif ex == "no" or ex == "No" or ex == "NO":
            print ("Say hi.")
elif remeber == "no" or remeber == "No" or remeber == "NO":
  remeber = input("Is there time to flee? (yes/no)")
  if remeber == "yes" or remeber == "Yes" or remeber == "YES":
    print ("Run for it.")
  elif remeber == "no" or remeber == "No" or remeber == "NO":
    remeber = input("Could you pretend to get a call on your cell? (yes/no)")
    if remeber == "yes" or remeber == "Yes" or remeber == "YES":
      print ("Hello, Doctor. What are my test results?")
    elif remeber == "no" or remeber == "No" or remeber == "NO":
      remeber = input("Are you wearing sunglasses? (yes/no)")
      if remeber == "yes" or remeber == "Yes" or remeber == "YES":
        print ("Keep walking.")
      elif remeber == "no" or remeber == "No" or remeber == "NO":
        print ("Address the person using an amusing nickname such as 'Sarge', 'Slugger', or 'Master Blaster'.")

