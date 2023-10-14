start = int( input() )
end = int( input() ) + 1
step = int( input() )

for f in range( start, end, step ):
    c = ( f - 32 ) * 5 / 9
    
    if c < 0:
        c = ceil( c )
    else:
        c = floor( c )
        
    print( f, c )
