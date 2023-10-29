def encode( message ):
    
    ans = []
    c, d = 0, "#"

    for ch in message:
        if ch == d:
            c += 1
        else:
            ans.append( d + str( c ) )
            d = ch
            c = 1

    ans.append( d + str( c ) )

    return "".join( ans[ 1 : ] )
