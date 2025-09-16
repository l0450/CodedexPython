# 06. Data Types
name = 'John'
age = 24
height = 1.80
male = True

# 07. Temperature
fahrenheit = 76
celcius = (fahrenheit - 32) / 1.8
print(celcius)

# 08. BMI
mass = 80
height = 1.80

bmi = mass / height ** 2
print(bmi)

# 09. Pythagorean Theorem
a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = (a**2 + b**2) ** 0.5

print(c)

# 10. Currency
peso = int(input("What do you have left in pesos? "))
sol = int(input("What do you have left in soles? "))
real = int(input("What do you have left in reais? "))

print((peso * 0.00026) + (sol * 0.29) + (real * 0.19))