def expression_matter( a, b, c ):
    if b == 1:
        if a == 1:
            if c == 1:
                return a + b + c
            else:
                return ( a + b ) * c
        elif a > c:
            return ( b + c ) * a
        else:
            return ( a + b ) * c
    elif a == 1:
        if c == 1:
            return a + b + c
        else:
            return ( a + b ) * c
    elif c == 1:
        return ( b + c ) * a
    else:
        return a * b * c
