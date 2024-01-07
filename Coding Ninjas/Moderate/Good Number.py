def isGoodNumber( n: int ) -> bool:
    
    s = { n }

    while n > 1:
        n = sum( int( i ) ** 2 for i in str( n ) )

        if n in s:
            return False
        else:
            s.add( n )

    return True
