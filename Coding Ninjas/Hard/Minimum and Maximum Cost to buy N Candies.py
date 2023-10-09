from math import ceil

def minimumCost( cost, n, k ):
    
    return sum( sorted( cost )[ : ceil( n / ( k + 1 ) ) ] )



def maximumCost( cost, n, k ):
    
    return sum( sorted( cost )[ -ceil( n / ( k + 1 ) ) : ] )
