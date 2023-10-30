def digitProduct( n: int ) -> int:

    a = []

    if n > 9:
        while n > 9:
            t = True

            for i in range( 9, 1, -1 ):
                if n % i == 0:
                    a.append( str( i ) )
                    n //= i
                    t = False

                    break

            if t:
                break
    else:
        for i in range( 2, 4 ):
            if n % i == 0:
                n //= i
                a.append( str( i ) )
                
    if n < 2 or n > 9:
        return -1
    else:
        a.append( str( n ) )

    return int( "".join( a[ : : -1 ] ) )
