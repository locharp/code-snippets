def derive( coefficient, exponent ): 
    
    coefficient *= exponent
    exponent -= 1
    
    return f"{ coefficient }x^{ exponent }"
