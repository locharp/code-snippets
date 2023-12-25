def checkMeta( str1, str2 ):

    n = len( str1 )

    if len( str2 ) != n:
        return False
        
    o = 0
    p = q = ""
    
    for i in range( n ):
        if str1[i] != str2[i]:
            if o < 1:
                p = str1[i]
                q = str2[i]
                o += 1
            elif o < 2:
                if p == str2[i] and q == str1[i]:
                    o += 1
                else:
                    return False
            else:
                return False

    return o == 2
