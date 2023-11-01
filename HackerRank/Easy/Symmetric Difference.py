input()
m = set( map( int, input().split() ) )
input()
n = set( map( int, input().split() ) )

for i in sorted( m ^ n ):
    print( i )
