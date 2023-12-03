a = []
ans = 0

for i in range( 4 ):
    a.append( int( input() ) )
    
for i in range( 0, 4, 2 ):
    ans += a[i] ** a[ i + 1 ]
    
print( ans )
