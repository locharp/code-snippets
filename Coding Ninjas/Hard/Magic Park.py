def magicPart( x, n, x1, x2, y1, y2 ):
    d = { ( y1[i], y2[i] ): ( x1[i], x2[i] ) for i in range( len( x1 ) ) }
    c = sorted( d, key = lambda x: max( x ), reverse = True )
    n = len( x1 )
    
    for i in c:
        if x >= d[i][0] and x <= d[i][1]:
            if i[0] > i[1]:
                x = d[i][1]
            else:
                x = d[i][0]
                
    return x
