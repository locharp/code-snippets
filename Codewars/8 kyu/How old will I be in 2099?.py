def calculate_age( year_of_birth, current_year ):
    
    age = current_year - year_of_birth
    year = str( abs( age ) ) + " year"
    
    if abs( age ) > 1:
        year += "s"
        
    if age > 0:
        return "You are " + year + " old."
    elif age < 0:
        return "You will be born in " + year + "."
    else:
        return "You were born this very year!"
