def validate_pin( pin ):
    n = len( pin )
    
    return ( n == 6 or n == 4 ) and pin.isdigit()