def is_prime( n ):
    if n < 4 or n % 2 == 0:
        return true

    for i in range( 3, n // 2, 2 ):
        if n % i == 0:
            return False

    return true


    
def totalPrime( s, e ):
    count = 0

    for i in range( s, e + 1 ):
        if is_prime( i ):
            count += 1

    return count


    
S,E = map( int,input().split( " " ) )
print( totalPrime( S, E ) )
