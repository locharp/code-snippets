def pushZerosAtEnd( arr ):
    i = j = 0
    
    while j < len( arr ):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
            
        j += 1
        
    for j in range( i, len( arr ) ):
        arr[j] = 0
        
    return arr
