def getLengthofLongestSubstring( s, k ):

    d = {}
    i = m = 0

    for j in range( len( s ) ):
        if s[j] in d:
            d[ s[j] ] += 1
        else:
            d[ s[j] ] = 1

        while len( d ) > k:
            d[ s[i] ] -= 1

            if d[ s[i] ] < 1:
                del d[ s[i] ]

            i += 1

        
        m = max( m, sum( d.values() ) )
        
    return m
