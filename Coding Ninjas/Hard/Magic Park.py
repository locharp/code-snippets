from collections import defaultdict

def magicPart( x, n, x1, x2, y1, y2 ):
    d = defaultdict( list )
    
    for i in range( n ):
        if y1[i] > y2[i]:
            d[ ( y1[i], y2[i] ) ].append( ( x1[i], x2[i] ) )
        else:
            d[ ( y2[i], y1[i] ) ].append( ( x2[i], x1[i] ) )
            
    c = sorted( d, key = lambda x: max( x ), reverse = True )
    y = 10001
    
    for j in c:
        if y < j[0]:
            continue
            
        for i in d[j]:
            if i[0] > i[1]:
                if x <= i[0] and x > i[1]:
                    x = i[1]
                    y = j[1]
                    break
            elif x >= i[0] and x < i[1]:
                x = i[1]
                y = j[1]
                break
                
    return x
