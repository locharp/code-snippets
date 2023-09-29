def isReflectionEqual( s ):
    for ch in "BCDEFGJKLNPQRSZ":
        if ch in s:
            return False
        
    return s == s[ : : -1 ]
