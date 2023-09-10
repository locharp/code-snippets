def addOneToNumber(arr):
    arr = [ 0 ] + arr
    arr[-1] += 1
    i = 0
    j = len( arr ) - 1
    
    while arr[j] > 9:
        arr[j] = 0
        j -= 1
        arr[j] += 1
        
    while arr[i] == 0:
        i += 1
        
    return arr[ i : ]