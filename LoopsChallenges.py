#  Are We There Yet?

answer = input("Are we there yet? ")

while answer != "Yes":
  answer = input("Are we there yet? ")

# New Year Countdown

for i in range(10, 0, -1):
    print(i)
    if i == 0:
      print("Happy New Year! 🥳")

# Snake Eyes

import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

total = die1 + die2

while total != 2:
   print("Nope")
   die1 = random.randint(1, 6)
   die2 = random.randint(1, 6)
   total = die1 + die2
print("Snake Eyes!")

# Asterisks

for i in range(1, 25):
    print('* ' * i)

# Sum of Squares

number = int(input("Enter the number: "))
total = 0

for i in range(1, number + 1):
  total += number ** 2

print(total)
