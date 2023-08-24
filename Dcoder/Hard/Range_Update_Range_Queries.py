n = int( input().split()[1] )
a = list( map( int, input().split() ) )

for _ in range( n ):
    q = tuple( map( int, input().split() ) )
   
    if q[0] == 1:
        print( min( a[ q[1] - 1 : q[2] ] ) )
    else:
        for i in range( q[1] - 1, q[2] ):
            a[i] += q[3]