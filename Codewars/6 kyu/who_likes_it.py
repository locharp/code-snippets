def likes( names ):
    n = len( names )
    m = ""
    
    if n < 1:
        m += "no one"
    elif n < 2:
        m += names[0]
    elif n < 3:
        m += names[0] + " and " + names[1]
    elif n < 4:
        m += f"{names[0]}, {names[1]} and {names[2]}" 
    else:
        m += f"{names[0]}, {names[1]} and { n - 2 } others"
        
    m += " likes this" if n < 2 else " like this"

    return m 
