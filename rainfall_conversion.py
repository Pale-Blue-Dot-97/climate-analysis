"""File containing functions to translate between rainfall units"""
def inches_to_mm(inches):
	"""
 	Converts rainfall in inches to mm

   	Args:
    		inches: Rainfall in inches

      	Returns:
       		Rainfall in mm
 	"""
	mm = inches * 25.4
	return mm
