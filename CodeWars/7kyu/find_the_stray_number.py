def stray( arr ):
    if arr[0] == arr[1]:
        if arr[0] == arr[2]:
            x = arr[0]
        else:
            return arr[2]
    elif arr[0] == arr[2]:
        return arr[1]
    else:
        return arr[0]
    
    for y in arr[ 3 : ]:
        if x != y:
            return y