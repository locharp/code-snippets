n = int( input() )

if n < 0:
    print( "Error" )
else:
    ans = 1
    
    for i in range( 2, n + 1):
        ans *= i
        
    print( ans )
