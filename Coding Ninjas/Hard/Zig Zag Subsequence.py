def zigZagSubsequence( tokenArray, count = 1, i = 1, o = 0 ):
    
    if i == len( tokenArray ):
        return count
    
    if o > 0:
        if tokenArray[ i - 1 ] > tokenArray[i]:
            count += 1
            o = -1
    elif o < 0:
        if tokenArray[ i - 1 ] < tokenArray[i]:
            count += 1
            o = 1
    else:
        count += 1
        o = tokenArray[i] - tokenArray[ i - 1 ]
        
    return zigZagSubsequence( tokenArray, count, i + 1, o )
