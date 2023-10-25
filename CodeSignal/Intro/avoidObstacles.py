def f( a, k ):
    t = True
    
    for i in range( k, a[-1] + k, k ):
        if i in a:
            t = False
            break
            
    if t:
        return k
    else:
        return f( a, k + 1 )
        
    
    
def solution( inputArray ):
    
    inputArray.sort()
    
    return f( inputArray, 2 )
