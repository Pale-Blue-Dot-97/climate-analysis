# Todo: Code is a bit unclear

def convert_fahr_to_celsius(fahr):
    celsius = (fahr - 32) * (5 / 9)
    return celsius

def convert_fahr_to_kelvin(fahr):
    celsius = convert_fahr_to_celsius(fahr)
    kelvin = celsius + 273.15
    return kelvin
