"""Module containing functions to convert temperatures between scales.

Functions:
    convert_fahr_to_celsius: Converts Fahrenheit to Celsius
    convert_fahr_to_kelvin: Converts Fahrenheit to Kelvin

Raises:
    ValueError: If temperature is impossible.
"""


def convert_fahr_to_celsius(fahr: float) -> float:
    """
    Converts Fahrenheit to Celsius.
    
    Args:
        fahr (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.

    Raises:
        ValueError: If temperature is impossible.
    """
    celsius = (fahr - 32) * (5 / 9)
    if celsius < -273.15:
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius

def convert_fahr_to_kelvin(fahr: float) -> float:
    """
    Converts Fahrenheit to Kelvin.

    Args:
        fahr (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Kelvin.
    """
    fahr = convert_fahr_to_celcius(x)
    kelvin = fahr + 273.15
    return kelvin
