# Codedex Python Course repo #

This repository is made for myself to learn and understand **Python** better.
I am using this website: https://www.codedex.io/python for this reason.
Below I will explain what tasks and exercises I have done.

----

## Chapter 1 ##

### 01. Setting up ###

Copying and pasting a single line of code that prints a message. Making sure
that when the code runs, the message appears on our terminal.

### 02. Hello World ###

Same as the exercise above, but the different message is being displayed.

### 03. Pattern ###

Creating a simple triangle pattern made with numbers and spaces. Multiple
print() methods required.

### 04. Initials ###

Displaying our initials with block letters. A single line comment has been added
to say a fun fact about the person holding those initials.

### 05. Snail Mail ###

A small letter with multiple print methods that says our goal after completing this course.

----

## Chapter 2 ##

### 06. Data types ###

Initializing 4 variables, each one with a different data type. Below I present the data
types I used:

- **String**
- **Integer**
- **Float**
- **Boolean**

### 07. Temperature ###

Simple temperature converter. The program converts the assigned temperature value from
Fahrenheit to Celcius (based on the formula for this purpose). After this, the result
is being printed out.

### 08. BMI ###

Similar to the previous example, I assigned both values (weight and height) by myself.
Based on those values, the program calculates the user's BMI. The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to quickly estimate body fat in certain populations. The formula is pretty simple: Take an individual's weight (mass) in kilograms and dividing it by their height in meters, squared.

### 09. Pythagorean Theorem ###

A **Pythagorean Theorem**  is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC. The program for this takes 3 values:

- The **a** which is the length of a short side.
- The **b** which is the length of another short side.
- The **c** which is the length of the hypotenuse.

The hypotenuse is the longest side of the right triangle. Program asks  the user for two numbers, a and b, and then calculates the hypotenuse c.

### 10. Currency ###

We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

- Colombian pesos
- Peruvian soles
- Brazilian reais

A program asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

----

## Chapter 3 ##

### 11. Coin Flip ###

All you need to know is that this program simulates a coin toss:

- 50% of the time, it's "Heads".
- 50% of the time, it's "Tails".

Run the program 5 times to get a taste of the if/else statement!

### 12. Grades ###

This program checks whether a grade is above or below the required exam result which is 55.
It starts by creating a variable called grade and give it a value between 0-100. Then I 
created a if/else statement that checks the result and prints out the message whether the
user passed the exam or not.

### 13. pH Levels ###

In chemistry, pH is a scale used to specify the acidity or basicity of a liquid. This piece
of code checks whether a pH level is basic, acidic, or neutral. First, a ph variable was
created and after that it asks the user for a value between 0 and 14:

- If ph is greater than 7, output "Basic".
- If ph is less than 7, output "Acidic".
- Else, output "Neutral".

### 14. Magic 8 Ball ###

The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. It's an oversized 8 ball with some of the following answers:

- **Yes - definitely.**
- **It is decidedly so.**
- **Without a doubt.**
- **Reply hazy, try again.**
- **Ask again later.**
- **Better not tell you now.**
- **My sources say no.**
- **Outlook not so good.**
- **Very doubtful.**

An easy program  that can respond to any Yes or No questions with a different answer each time it executes.

### 15. The Cyclone ###

Since 1927, "The Cyclone" roller coaster has delighted visitors at Coney Island (Brooklyn, NY).
They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and I needed your help writing the program for it! The program asks the user what their height is and how many credits they have, and store the values in a **height** variable and a **credits** variable.
Below I present the rules about what are the requirements to use this roller coaster:

- If they are tall enough and have enough credits, print "Enjoy the ride!"
- Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride"
- Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
- Else, print a message saying they have not met either requirement.

### 16. Sorting Hat ###

The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

- **Gryffindor**
- **Slytherin**
- **Hufflepuff**
- **Ravenclaw**

The Sorting Hat asks the user some questions with the int() and input() functions. Based on the answers, the program selects the house you will represent at Hogwarts!

----

## Control flow challenges ##

### Food ratings ###

In a five-star restaurant review system, the stars typically represent the different levels of satisfaction.

But what does each of the stars mean?

Start by creating a rating variable and set it equal to a decimal number.

Make a rating system using an if/elif/else statement:

- Rating greater than 4.5, print 'Extraordinary'
- Rating greater than 4, print 'Excellent'
- Rating greater than 3, print 'Good'
- Rating greater than 2, print 'Fair'
- Everything else, print 'Poor'

### High School Grades ###

U.S. high schools typically last for four years, from freshman year to senior year.

First, ask the user to enter their grade as an integer.

Create a four-year high school grade system using an if/elif/else statement:

- Grade is 9, print 'Freshman'
- Grade is 10, print 'Sophomore'
- Grade is 11, print 'Junior'
- Grade is 12, print 'Senior'
- Everything else is 'TBD'

### Snapple Facts ###

Snapple is a famous tea drink brand from Queens, New York. Each bottle cap comes with a silly fun fact.

Use the random module to create a number from 0 to 5.

Then use an if/elif/else statement to print out one of these six random Snapple facts:

- 0 - 'Flamingos turn pink from eating shrimp.'
- 1 - 'The only food that doesn\'t spoil is honey.'
- 2 - 'Shrimp can only swim backwards.'
- 3 - 'A taste bud\'s life span is about 10 days.'
- 4 - 'It is impossible to sneeze while sleeping.'
- 5 - 'It is illegal to sing off-key in North Carolina.'

### Seasons of the Year ###

Ah, the four seasons in the year — winter, spring, summer, or fall; all you have to do is call!

Ask the user the month number using the input() function.

Check for the four seasons using an if/elif/else statement and logical operators:

- Month is 1, 2, 3, print 'Winter 🌨️'
- Month is 4, 5, 6, print 'Spring 🌱'
- Month is 7, 8, 9, print 'Summer 🌻'
- Month is 10, 11, 12, print 'Autumn 🍂'
- Everything else is 'Invalid'

### Planet Weights ###

The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

Create a weight conversion program that:

- Asks the user what their Earth weight is (as a float).
- Asks the user for a planet number (as an int).

Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:

destination weight= Earth weight × relative gravity

If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.





