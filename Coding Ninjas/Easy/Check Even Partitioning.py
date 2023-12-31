def checkEvenPartitioning( n ):
    
    if n < 4:
        return False
    else:
        return n % 2 < 1
