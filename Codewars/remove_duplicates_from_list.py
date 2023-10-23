def distinct( seq ):
    a = []
    
    for i in seq:
        if i not in a:
            a.append( i )
            
    return a
