def solution( picture ):
    
    c = len( picture[0] ) + 2
    
    return [ "*" * c,  *( "*" + row + "*" for row in picture ), "*" * c ]
