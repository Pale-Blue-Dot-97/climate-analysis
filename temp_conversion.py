"""
A module for converting temperature from imperial to metric units
Will throw ValueErrors for temperature < absolute zero

Functions:
    convert_fahr_to_celsius: convert Fahrenheit to Celsius
    convert_fahr_to_kelvin: converts Fahrenheit to Kelvin
"""

# Todo: Code is a bit unclear

def convert_fahr_to_celsius(fahr):
    """
    Given a temperature in Fahrenheit, converts it to Celsius

    :param fahr: the temperature in Fahrenheit
    :raises ValueError: if the temperature is below absolute zero
    :return: the temperature in Celsius
    """
    celsius = (fahr - 32) * (5 / 9)
    if celsius < -273.15:
        # If temperature is below absolute zero. throw an error.
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius

def convert_fahr_to_kelvin(fahr):
    celsius = convert_fahr_to_celsius(fahr)
    kelvin = celsius + 273.15
    return kelvin
