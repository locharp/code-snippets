def solution( inputString ):
    
    a = inputString.split( "." )
    
    if len( a ) != 4:
        return False
        
    for i in a:
        if not i.isdecimal() or ( len( i ) > 1 and i[0] == "0" ):
            return False
            
        i = int( i )
        
        if i < 0 or i > 255:
            return False
            
    return True
