def descending_order( num ):
    arr = []
    
    while num > 0:
        arr.append( num % 10 )
        num //= 10
        
    for i in sorted( arr )[ : : -1 ]:
        num = num * 10 + i
        
    return num