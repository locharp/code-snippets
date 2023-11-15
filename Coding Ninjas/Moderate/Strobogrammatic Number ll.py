from itertools import product

def findStrobogrammatic( n ):
    
    c = product( "01689", repeat = n // 2 )
    d = { "0": "0", "1": "1", "6": "9", "8": "8", "9": "6" }
    m = []
    ans = []
    
    if n < 2:
        return [ "0", "1", "8" ]
    elif n % 2 > 0:
        m = [ "0", "1", "8" ]
    else:
        m = [ "" ]

    for i in c:
        if i[0] == "0":
            continue
            
        j = [ d[k] for k in i[ : : -1 ] ]
        
        for k in m:
            ans.append( "".join( i ) + k + "".join( j ) )
    
    return ans
