# print greeting text for the love calculaor
print("The Love Calculator is calculating your score...")

#input the names 
name1 = input("What is your name?\n ")
name2 = input("What is your partner's name?\n ")

#combine both names
combine_names = name1 + name2

# make the letters to lower case
lower_names = combine_names.lower()

# find the count of "T" "R" "U" "E" and add it as the first digit
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

# find the count of "L" "O" "V" "E" and add it as the second digit
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

# add the first and second digit together and give result
result = int(str(first_digit) + str(second_digit))

# check if the result is less than 10 or greater than 90
if (result < 10) or (result > 90):
  print(f"Your score is {result}, you go together like coke and mentos.")

# check if the result is greater than or equals to 40 and less than or equals to 50
elif (result >= 40) and (result <= 50):
  print(f"Your score is {result}, you are alright together.")
  
# check if the result is not satisfying the condition
else:
  print(f"Your score is {result}.")
  print('''
*************************************
''')
  print(f"        {name1}")
  print('''
*************************************

88                                     
88                                     
88                                     
88  ,adPPYba,  8b       d8  ,adPPYba,  
88 a8"     "8a `8b     d8' a8P_____88  
88 8b       d8  `8b   d8'  8PP"""""""  
88 "8a,   ,a8"   `8b,d8'   "8b,   ,aa  
88  `"YbbdP"'      "8"      `"Ybbd8"'

*************************************
''')
  print(f"        {name2}")
  print('''
*************************************
''')
