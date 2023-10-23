def warn_the_sheep( queue ):
    n = len( queue ) - 1
    m = queue.index( "wolf" )
    
    if m == n:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number " + str( n - m ) + "! You are about to be eaten by a wolf!"
