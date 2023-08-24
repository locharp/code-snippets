n = int( input() )

for i in range( 1, n + 1 ):
    s = "1"
    
    for j in range( 2, i + 1 ):
        s = str( j ) + s + str( j )
       
    print( " " * ( n - i ) + s )