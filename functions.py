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
def day_of_week(day_number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns a string representing the corresponding day of the week
    -------------------------------------------------------
    Parameters:
        day_number - a day of the week as a number(int > 0)
    Returns:
        day - a day of the week as a string(str)
    ------------------------------------------------------
    """
    if day_number == 1:
        day = 'Monday'
    elif day_number == 2:
        day = 'Tuesday'
    elif day_number == 3:
        day = 'Wednesday'
    elif day_number == 4:
        day = 'Thursday'
    elif day_number == 5:
        day = 'Friday'
    elif day_number == 6:
        day = 'Saturday'
    elif day_number == 7:
        day = 'Sunday'
    else:
        day = 'Error'
    return day