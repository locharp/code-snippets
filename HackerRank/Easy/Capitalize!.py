def solve( s ):
    
    a = list( s )
    t = True
    
    for i in range( len( a ) ):
        if a[i] == " ":
            t = True
        else:
            if t:
                a[i] = a[i].upper()
                t = False
            
    return "".join( a )
    
