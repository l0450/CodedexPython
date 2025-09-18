# Food rating
rating = 4.1

if rating > 4.5:
  print('Extraordinary')
elif rating > 4:
  print('Excellent')
elif rating > 3:
  print('Good')
elif rating > 2:
  print('Fair')
else:
  print('Poor')

# High school grades

grade = int(input("Enter your grade: "))

if grade == 9:
  print('Freshman')
elif grade == 10:
  print('Sophomore')
elif grade == 11:
  print('Junior')
elif grade == 12:
  print('Senior')
else:
  print('TBD')

# Snapple Facts

import random

number = random.randint(0, 5)

if number == 0:
  print('Flamingos turn pink from eating shrimp.')
elif number == 1:
  print('The only food that doesn\'t spoil is honey.')
elif number == 2:
  print('Shrimp can only swim backwards.')
elif number == 3:
  print('A taste bud\'s life span is about 10 days.')
elif number == 4:
  print('It is impossible to sneeze while sleeping.')
elif number == 5:
  print('It is illegal to sing off-key in North Carolina.')

# Seasons of the Year

month = int(input("Give me the number: "))

if month == 1 or month == 2 or month == 3:
  print('Winter 🌨️')
elif month == 4 or month == 5 or month == 6:
  print('Spring 🌱')
elif month == 7 or month == 8 or month == 9:
  print('Summer 🌻')
elif month == 10 or month == 11 or month == 12:
  print('Autumn 🍂')
else:
  print('Invalid')

# Planet Weights

earthweight = float(input("Please enter your weight: "))
planet = int(input("What planet are you in?: "))

if planet == 1:
  destination_weight = earthweight * 0.38
  print(destination_weight)
elif planet == 2:
  destination_weight = earthweight * 0.91
  print(destination_weight)
elif planet == 3:
  destination_weight = earthweight * 0.38
  print(destination_weight)
elif planet == 4:
  destination_weight = earthweight * 2.53
  print(destination_weight)
elif planet == 5:
  destination_weight = earthweight * 1.07
  print(destination_weight)
elif planet == 6:
  destination_weight = earthweight * 0.89
  print(destination_weight)
elif planet == 7:
  destination_weight = earthweight * 1.14
  print(destination_weight)
else:
  print('Invalid planet number')
