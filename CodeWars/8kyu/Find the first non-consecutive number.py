def first_non_consecutive( arr ):
    for i in range( 1, len( arr ) ):
        if arr[ i - 1 ] + 1 != arr[i]:
            return arr[i]
        
    return None