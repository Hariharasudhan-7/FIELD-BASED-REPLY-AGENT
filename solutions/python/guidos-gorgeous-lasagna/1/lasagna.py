"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME =  40


def bake_time_remaining(a)-> int :
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    bake_timeremaining = EXPECTED_BAKE_TIME - a 
    return bake_timeremaining

def preparation_time_in_minutes(layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - total preparation time.
    """
    return layers*2
    
def elapsed_time_in_minutes(number_of_layers, time_in_oven):
    """
    Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of lasagna layers
    :param time_in_oven: int - time already spent baking
    :return: int - total time spent preparing and baking
    """
    elapsed_time = (number_of_layers * 2) + time_in_oven
    return elapsed_time

    
print(elapsed_time_in_minutes(2,30))