def printer_error( s ):
    ans = 0
    
    for ch in s:
        if ch in "nopqrstuvwxyz":
            ans += 1
            
    return str( ans ) + "/" + str( len( s ) )