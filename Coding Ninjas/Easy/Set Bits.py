def countBits( n ):
    return bin( n ).count( "1" )



n = int( input() )
print( countBits( n ) )
