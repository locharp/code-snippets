def get_middle( s ):
    
    i = len( s )
    
    if i < 1:
        return ""
    elif i % 2 < 1:
        return s[ i // 2 - 1 : i // 2 + 1 ]
    else:
        return s[ i // 2 ]
