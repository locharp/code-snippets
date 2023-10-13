def areIsomorphic( str1: str, str2: str ) -> bool:
    n = len( str1 )
    
    if n != len( str2 ):
        return 0
    
    d, e = {}, {}
    
    for i in range( len( str1 ) ):
        if str1[i] not in d:
            if str2[i] in e:
                return 0
            
            d[ str1[i] ] = str2[i]
            e[ str2[i] ] = str1[i]
        elif d[ str1[i] ] != str2[i]:
            return 0
            
    return 1
