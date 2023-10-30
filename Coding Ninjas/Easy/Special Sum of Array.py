def specialSum(arr, n):
    
    while len( arr ) > 1:
        arr = [ int( i ) for i in str( sum( arr ) ) ]

    return arr[0]
