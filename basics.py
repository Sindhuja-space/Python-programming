'''
VARIABLE:

full_name = "John Smith"
age = 20
is_new = True


INPUT:

name = input("Enter your name: ")
favorite_color = input("Enter your favorite color:")
print(name + " likes " + favorite_color)


WEIGHT CONVERSION:

weight_lbs = int(input("Enter your weight(lbs): "))
weight_kg = weight_lbs * 0.45359237
print(weight_kg,"kg")


DOWN PAYMENT:

house_price = 1000000
good_credit = False

if good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price

print(f"Down Payment is: ${down_payment}")


WEIGHT CONVERSION:

weight = float(input("Enter your Weight: "))
weight_unit = input("(L)bs or (k)g: ")

if weight_unit.upper() == "L":
    kilogram = weight * 0.45
    print(f"You are {kilogram} kilos")
else:
    pounds = weight / 0.45
    print(f"You are {pounds} pounds")

    
GUESSING GAME:

secret_number = 9
guess_count = 0 
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Make a Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break 
else:
    print("Sorry, You Failed")


CAR GAME:
    
command = ""
started = False 

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - quit to quit""")
    elif command == "quit":
        break
    else:
        print("I don't understand that!")

        
F SHAPE PATTERN:

numbers = [5,2,5,2,2]

for number in numbers:
    print(number * 'x')


FIND MAXIMUM:    

numbers = [10,30,50,80,20,40,60,90,70]
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number
print(maximum)


UNIQUE NUMBERS:

numbers = [1,2,3,1,2,3,4,5,5,6]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

'''

import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second 
    

dice = Dice()
print(dice.roll())
       
    
























