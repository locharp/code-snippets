def increment_string( strng ):
    
    n = len( strng )
    i = n - 1
    
    while i >= 0 and strng[i].isdecimal():
        i -= 1
        
    i += 1
    
    if i == n:
        return strng + "1"
    
    s = strng[ i : ]
    t = str( int( s ) + 1 ).zfill( n - i )
    
    return strng[ : i ] + t
