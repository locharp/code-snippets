def stringMania( n : int, m : int, str1 : str, str2 : str ) -> int:
    for i in range( min( m, n ) ):
        if str1[i] > str2[i]:
            return 1
        elif str2[i] > str1[i]:
            return -1
        
    if n > m:
        return 1
    elif m > n:
        return -1
    else:
        return 0
