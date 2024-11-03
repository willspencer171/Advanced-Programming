# Program to use converters

import Converters
print("Select conversion:")
print("\t1. Grams(g) To Pounds(lbs)")
print("\t2. Grams(g) To Ounces(oz)")
print("\t9. Exit")
user = int(input(">> "))

if user == 1:
    grams = int(input("Enter value in Grams: "))
    pounds = Converters.gramsTolbs(grams)
    print(f"{grams}g is {pounds:.6f}lbs")
elif user == 2:
    grams = int(input("Enter value in Grams: "))
    ounces = Converters.gramsToOunce(grams)
    print(f"{grams}g is {ounces:.6f}lbs")
elif user == 9:
    print("Program Exiting")
else:
    print("Invalid Input")
