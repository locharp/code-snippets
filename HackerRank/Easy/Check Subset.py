for i in range( int( input() ) ):
    input()
    s1 = set( map( int, input().split() ) )
    input()
    s2 = set( map( int, input().split() ) )
    
    print( s1.issubset( s2 ) )
