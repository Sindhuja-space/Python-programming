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

'''

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














