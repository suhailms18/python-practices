# welcome note
print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")

print('You are currently in a dark forest and you see a path to the woods to the "right" and a path to the sea to the "left".')

# input the value as the first choice
choice1 = input("Wich way do you want to go? Right or Left?\n").lower()

# creating conditions
if choice1 == "left":
  # input the value as the second choice
  choice2 = input("You have passed the first challenge. Now you are beside of the river. How you want to go? Wait for a boat or Swim?\n").lower()
  
  if choice2 == "wait":
    # input the value as the third choice
    choice3 = input("You have passed the second challenge. There is a house with 3 doors. One red, one yellow and on blue. Which colour do you choose?\n").lower()
    if choice3 == "red":
      print("It is a room full of fire. Game over!")
    elif choice3 == "yellow":
      print('''
*******************************************************************************
''')
      print("            You have entered the room of treasure. You win!")
      print('''
_______________________________________________________________________________
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    elif choice3 == "blue":
      print("You have entered the room of beasts. Game over!")
    else:
      print("You got attacked by an angry trout. Game over!")
  elif choice2 == "swim":
    print("Oops, the crocodiles got that. Game over!")
elif choice1 == "right":
  print("You chose the wrong path. Fell into the digging trap and died. Game over!")
  quit()
else:
  print("You are not following the rule. Throwing out!")
  quit()

