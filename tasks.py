from functions import feet_to_acres
from functions import mow_lawn
from functions import date_extract
from functions import multiply_fractions
from functions import math_quiz

'''
#task 1
square_footage = float(input("Square footage: "))
print()
print(f"{feet_to_acres(square_footage):,.2f} acres is equivalent to {square_footage:,.2f} square feet")
'''

'''
#task 2

width = float(input("Width (m): "))
length = float(input("Length (m): "))
speed = float(input("Speed (m^2/minute): "))
print()
print(f"Mowing the lawn takes {mow_lawn(width, length, speed):.0f} minutes")
'''

'''
#task 3
date_number = int(input("Enter a date in the format MMDDYYYY: "))
print()
year, month, day = date_extract(date_number)
print(f"The reformatted date: {year}/{month:02}/{day:02}")
'''

'''
#task 4
num1 = int(input("Numerator 1: "))
denom1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
denom2 = int(input("Denominator 2: "))

numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
print()
print(f"Result: {numerator}/{denominator} = {product:.3f}")
'''

#task 5
math_quiz()
