"""
-------------------------------------------------------
[Lab 05, Functions]
-------------------------------------------------------
Author:  Carlos Alcoba
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""
from random import randint

# constants
SQRTOACRE = 43560 #square feet per acre


#functions
#t01
def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    return square_footage / SQRTOACRE

#t02
def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    total_area = width * length
    time = total_area / speed
    return time


#t03
def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    day = (date_number // 10000) % 100
    month = date_number // 1000000
    year = date_number % 10000

    return year, month, day

#t04
def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    numerator = num1 * num2
    denominator = denom1 * denom2
    product = (num1 / denom1) * (num2 / denom2)
    return numerator, denominator, product

#t05
def math_quiz():
    """
    -------------------------------------------------------
    Creates a simple math quiz where two random numbers need
    to be added
    Use: math_quiz()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        None
    ------------------------------------------------------
    """
    num1 = randint(0, 999)
    num2 = randint(0, 999)
    answer = num1 + num2
    print(f"{num1:>5}")
    print(f"+ {num2:>3}")
    print()
    user_answer = int(input("Your answer: "))
    print()
    print(f"Your answer: {user_answer:>4}")
    print(f"Expected: {answer:>7}")

    return
