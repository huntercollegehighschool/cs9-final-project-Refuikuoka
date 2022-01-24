"""
Name(s): Rei Fukuoka
Name of Project: Prison Break
"""

#Write the main part of your program here. Use of the other pages is optional.
import time
import os

cutters = int(0)
file = int(0)
bed_dummy = int(0)
outfit = int(0)

def gameover():
  time.sleep(3)
  print("\nThe guards take hold of you, and throw you into the solitary. \nYou will restart.")
  time.sleep(5)
  os.system('clear')
  
  game1()

def intro():
  print("Sunday, New York 5:00 AM")
  time.sleep(2.0)
  print("\nYou wake up at the noise of a screeching alarm, inside a prison cell.")
  time.sleep(3.0)
  print("\nYou remember: Despite arguing countless times that you did \nnot commit the crime, you were falsely accused and sentenced \nto 30 years of prison.")
  time.sleep(4.0)
  print("\nBut, you cannot wait that long. You decide to escape.")

def take_cutter():
  global cutters
  print("\nHowever, if you take the cutters, the maintenance workers \nmay notice you and you could get in trouble.")
  cut = input("\nDo you take the cutters? (Type 1 for yes, 2 for no): ")

  while cut not in [str(i) for i in range(1,3)]:
    print("That is not a valid choice.")
    time.sleep(2)
    os.system('clear')
    cut = input("Do you take the cutters? (Type 1 for yes, 2 for no): ")
  
  if cut == "1":
    print("\nYou carefully slide the cutters inside your pocket.")
    time.sleep(1)
    print("\nThankfully, the maintenance workers do not notice!")
    cutters = cutters + 1
  elif cut == "2":
    print("\nYou think safely, and decide not to take the cutters.")

def take_guardoutfit1():
  global file
  time.sleep(3)
  print("\nHowever, if you take the guard's outfit, the guards \nmay notice you and you could get in big trouble.")
  time.sleep(3)
  outfit = input("\nDo you take the guard's outfit? (Type 1 for yes, 2 for no): ")

  while outfit not in [str(i) for i in range(1,3)]:
    print("That is not a valid choice.")
    time.sleep(2)
    os.system('clear')
    outfit = input("\nDo you take the guard's outfit? (Type 1 for yes, 2 for no): ")
  
  if outfit == "1":
    print("\nYou carefully take the guard's outfit.")
    time.sleep(2)
    print("\n...Or not carefully. The guards notice you taking the clothes.") 

    gameover()
  elif outfit == "2":
    print("\nYou think safely, and decide not to take the guard's outfit.")
    time.sleep(2)
    print("\nOn the way back to your prison cell, you find a metal file in a garbage can.")
    time.sleep(2)
    print("\nIt is rusty, but you could use it to cut fences.\nYou pick them up, and bring them to your cell.")

    file = file + 1
    
def choice2():
 choice2 = input("\nWhere will you go? (Type in 1 for maintenance or 2 for guard): ")

 while choice2 not in [str(i) for i in range(1,3)]:
  print("You cannot go there.")
  time.sleep(2)
  os.system('clear')
  choice2 = input("\nWhere will you go? (Type in 1 for maintenance or 2 for guard): ")

  if choice2 == "1":
    print("\nYou decide to go to the maintenance office.")
    time.sleep(1.5)
    print("\nHowever, you do not find anything there.")
    time.sleep(2)
    print("\nYou go back to your prison cell.")
  
  elif choice2 == "2":
    print("\nYou decide to go to the guard's office.")
    time.sleep(1.5)
    print("\nThere, you find an extra guard outfit!")
    time.sleep(1)
    print("\nThey may be useful to escape, allowing you to \nwalk around at night without being suspicious.")

    take_guard2()

def take_guard2():
  global outfit
  time.sleep(2)
  print("Luckily, there are no guards around.")
  time.sleep(1.5)
  outfit2 = input("\nDo you take the guard's outfit? (Type 1 for yes, 2 for no): ")

  while outfit2 not in [str(i) for i in range(1,3)]:
    print("That is not a valid choice.")
    time.sleep(2)
    os.system('clear')
    outfit2 = input("\nDo you take the guard's outfit? (Type 1 for yes, 2 for no): ")

  if outfit2 == "1":
    print("\nYou take the outfit, and run back to your cell.")
    time.sleep(1)
    print("\nFortunately, no one notices you.")
    outfit = outfit + 1
  elif outfit2 == "2":
    print("\nYou think safely, and decide not to take the outfit.")
    time.sleep(2)
    print("\nYou return to your prison cell.")

def trade():
  global bed_dummy
  print("\nYou ask him what the 'valuable' information is, \nbut he won't tell you.")
  time.sleep(1.7)
  trade = input("\nWill you trade your food for valuable information? (Type 1 for yes, 2 for no): ")  

  while trade not in [str(i) for i in range(1,3)]:
    print("That is not a valid choice.")
    time.sleep(2)
    os.system('clear')
    trade = input("Will you trade your food for valuable information? (Type 1 for yes, 2 for no): ")  
  
  if trade == "1":
    print("\nYou give him your loaf of bread.")
    time.sleep(1)
    print("\nHe thanks you, and tells you how to create a bed dummy, \nwhich makes it look as though you are sleeping in bed when you are not. ")
    time.sleep(8)
    print("\nAfter breakfast, you go back to your prison cell and craft a bed dummy.")
    time.sleep(5)
    print("You're to hungry to do anything during free time, and rest in your bed.")
    bed_dummy = bed_dummy + 1
  elif trade == "2":
    print("\nYou don't trust him, and refuse to give your food to him.")
    time.sleep(2)
    print("\nIt is now free time. You may choose to go to the maintenance office or the guard's office.")
    choice2 = input("\nWhere will you go? (Type in 1 for maintenance or 2 for guard): ")

    while choice2 not in [str(i) for i in range(1,3)]:
      print("You cannot go there.")
      time.sleep(2)
      os.system('clear')
      choice2 = input("\nWhere will you go? (Type in 1 for maintenance or 2 for guard): ")

    if choice2 == "1":
      print("\nYou decide to go to the maintenance office.")
      time.sleep(1.5)
      print("\nHowever, you do not find anything there.")
      time.sleep(2)
      print("\nYou go back to your prison cell.")
  
    elif choice2 == "2":
      print("\nYou decide to go to the guard's office.")
      time.sleep(1.5)
      print("\nThere, you find an extra guard outfit!")
      time.sleep(1)
      print("\nThey may be useful to escape, allowing you to \nwalk around at night without being suspicious.")

      take_guard2()



def day1():
  print("\nDAY 1")
  time.sleep(0.5)
  print("\nYou go to roll call and eat breakfast. \nNow, you have one hour of free time until work time.")

  choice1 = input("\nYou can decide to go to the Maintenance \noffice or the Guard's office.\n\nWhere will you go? (Type in 1 for maintenance or 2 for guard): ")

  while choice1 not in [str(i) for i in range(1,3)]:
    print("You cannot go there.")
    time.sleep(2)
    os.system('clear')
    choice1 = input("\nYou can decide to go to the Maintenance \noffice or the Guard's office.\n\nWhere will you go? (Type in 1 for maintenance or 2 for guard): ")

  if choice1 == "1":
    print("\nYou decide to go to the maintenance office.")
    time.sleep(1.5)
    print("\nThere, you find a pair of cutters!")
    time.sleep(1)
    print("They may be useful to escape.")
  
    take_cutter()
  
    print("\nYou come out of the maintenance office, \nand realize it is work time. \n\nYou run to the working area.")
  
  elif choice1 == "2":
    print("\nYou decide to go to the guard's office.")
    time.sleep(1.5)
    print("\nThere, you find an extra guard outfit.")
    time.sleep(1)
    print("\nThey may be useful to escape, allowing you to \nwalk around at night without being suspicious.")

    take_guardoutfit1()

def day2():
  os.system('clear')
  print("DAY 2")
  time.sleep(0.5)
  print("\nYou go to roll call, and go to the cafeteria.")
  time.sleep(2)
  print("\nYou're about to start eating your food, when, \nthe person next to you starts talking to you.")
  time.sleep(2)
  print("\nHe tells you that he will give you \nvaluable information for your food. ")
  time.sleep(3)
  trade()

def day2_2():
  time.sleep(2)
  os.system('clear')
  print("You go to the evening roll call, and are told that \nyour prison cell will be checked thoroughly for \ncontraband items on day 4.")
  time.sleep(5)
  print("\nIf contraband items are found, you will get in big trouble. \n\nKnowing that you have lots of items that you prepared to escape the prison, you make a decision to escape tomorrow night.")
  
def day3():
  os.system('clear')
  print("DAY 3")
  time.sleep(0.5)
  print("You wait until nightfall. When all lights have been shut down, you start executing your plan.")

  if cutters == 1 and bed_dummy == 1:
    print("\nYou take out your bed dummy, and place it on your bed.")
    time.sleep(2)
    print("\nYou sneak out of your cell, and carefully walk outside, near the outer fences.")
    time.sleep(2)
    print("\nYou take out your pair of cutters, and start cutting the fence...")
    time.sleep(3)
    print("\nAfter about an hour, you finish cutting a hole in the fence.")
    time.sleep(2)
    print("\nYou squeeze yourself into the hole, and outside the prison. \n\nCongrats! You have escaped!!")
  elif file == 1 and outfit == 1:
    print("\nYou take out the guard_outfit and put it on.")
    time.sleep(2)
    print("\nYou then go to the guard's office, telling \nthe other guards that you have checked \nthe cells of all prisoners.")
    time.sleep(3)
    print("\nYou walk outside near the outer fences, and you pull out your metal file.")
    time.sleep(2)
    print("\nYou slowly start cutting a hole with the file, \nand after about an hour, you finish cutting!")
    time.sleep(4)
    print("\nYou squeeze yourself into the hole, and outside the prison. \n\nCongrats! You have escaped!!")
  elif cutters == 1 and outfit == 1:
    print("\nYou take out the guard_outfit and put it on.")
    time.sleep(2)
    print("\nYou then go to the guard's office, telling \nthe other guards that you have checked \nthe cells of all prisoners.")
    time.sleep(3)
    print("\nYou walk outside near the outer fences, and you pull out your cutters.")
    time.sleep(2)
    print("\nYou slowly start cutting a hole with the cutters, \nand after about an hour, you finish cutting!")
    time.sleep(4)
    print("\nYou squeeze yourself into the hole, and outside the prison. \n\nCongrats! You have escaped!!")
  elif cutters == 1 and bed_dummy == 0 and outfit == 0:
    print("\nYou sneak out of your cell, and carefully walk outside, near the outer fences.")
    time.sleep(2)
    print("\nYou take out your pair of cutters, and start cutting the fence...")
    time.sleep(3)
    print("\nWhen, suddenly, the alarm goes off.")
    time.sleep(2)
    print("It looks like the guards found out you were not in your bed.")
    time.sleep(2)
    print("You see a guard running towards you.")
    time.sleep(20)
    gameover()
  elif file == 1 and bed_dummy == 0 and outfit == 0:
    print("\nYou sneak out of your cell, and carefully walk outside, near the outer fences.")
    time.sleep(2)
    print("\nYou take out your metal file, and start cutting the fence...")
    time.sleep(3)
    print("\nWhen, suddenly, the alarm goes off.")
    time.sleep(2)
    print("It looks like the guards found out you were not in your bed.")
    time.sleep(2)
    print("You see a guard running towards you.")
    time.sleep(20)
    gameover()
  elif cutters == 0 and file == 0:
    print("\nYou sneak out of your cell, and carefully walk outside.")
    time.sleep(2)
    print("\nHowever, you see the outer fences. \nYou have no tool to cut it through. \nJust then, you see a guard running towards you.")
    time.sleep(20)
    gameover()
  elif file == 1 and outfit == 0:
    print("\nYou walk outside near the outer fences, and you pull out your metal file.")
    time.sleep(2)
    print("\nYou slowly start cutting a hole with the file, \nwhen you notice a guard is passing near you.")
    time.sleep(3)
    print("You try quickly to hide, but the guard notices you.")
    time.sleep(20)
    gameover()


def game():
  intro()
  time.sleep(3)
  day1()
  time.sleep(10)
  day2()
  time.sleep(10)
  day2_2()
  time.sleep(15)
  day3()


def game1():
  print("After being in the solitary for a month, \nyou are finally let out. ")
  time.sleep(3)
  print("\nYou still haven't lost hope. You will plan to escape once again.")
  time.sleep(5)
  day1()
  time.sleep(10)
  day2()
  time.sleep(10)
  day2_2()
  time.sleep(15)
  day3()

game()



#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
