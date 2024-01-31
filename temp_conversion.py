"""Module containing functions to convert temperatures between scales."""


def convert_fahr_to_celcius(fahr):
    """
    Converts Fahrenheit to Celcius.
    
    Args:
        fahr: Temperature in Fahrenheit.

    Returns:
        Temperature in Celcius.
    """
    celcius = (fahr - 32) * (5 / 9)
    return celcius

def convert_fahr_to_kelvin(fahr):
    """
    Converts Fahrenheit to Kelvin.

    Args:
        fahr: Temperature in Fahrenheit

    Returns:
        Temperature in Kelvin.
    """
    fahr = convert_fahr_to_celcius(x)
    kelvin = fahr + 273.15
    return kelvin
