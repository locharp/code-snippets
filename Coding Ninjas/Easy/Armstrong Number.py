def isArmstrong( num ):
    s = str( num )
    n = len( s )
    total = 0
    
    for ch in s:
        total += int( ch ) ** n
        
    return total == num