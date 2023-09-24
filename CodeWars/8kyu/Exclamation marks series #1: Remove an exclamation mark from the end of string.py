def remove( s ):
    if len( s ) < 1:
        return s
        
    return s[ : -1 ] if s[-1] == "!" else s
