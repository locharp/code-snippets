def sum_of_differences( arr ):
    
    if len( arr ) < 1:
        return 0
    
    arr.sort()

    return arr[-1] - arr[0]
