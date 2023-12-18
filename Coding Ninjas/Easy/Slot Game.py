def alotAcore( original, guess ):
    
    ans = 0
    c = { "R": 0, "Y": 0, "G": 0, "B": 0 }
    d = { "R": 0, "Y": 0, "G": 0, "B": 0 }
    
    for i in range( len( guess ) ):
        c[ original[i] ] += 1
        d[ guess[i] ] += 1
       
        if original[i] == guess[i]:
            ans += 1
           
    for i in c:
        ans += min( c[i], d[i] )
       
    return ans
