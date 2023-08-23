n = int( input() ) + 1
ans = [ { "()" } ] + [ set() for _ in range( n - 2 ) ]

for i in range( 2, n ):
    for p in ans[ i - 2 ]:
        ans[ i - 1 ].update( ( "()" + p, p + "()", "(" + p +")" ) )
        
    for j in range( 2, i // 2 + 1 ):
        for p in ans[ j - 1 ]:
            for q in ans[ i - j - 1 ]:
                ans[ i - 1 ].update( ( p + q, q + p ) )
                
for p in ans[-1]:
    print( p )
