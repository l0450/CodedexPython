# 17. Enter PIN

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')

# 18. Guess number

guess = 0
tries = 0;

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1
  

print("You got it!")

# 19. Detention

for i in range(101):
  print("I will not use Snapchat in class")

# 20. 99 Bottles

for i in range(99, 0, -1):
      print(i, "bottles of beer on the wall,", i, "bottles of beer.")
      print("Take one down and pass it around,", i - 1, "bottles of beer on the wall.\n")

# 21. Fizz Buzz

for i in range(1, 101):
      if i % 3 == 0 and i % 5 == 0:
       print("FizzBuzz")
      elif i % 3 == 0:
       print("Fizz")
      elif i % 5 == 0:
       print("Buzz")
      else:
       print(i)

