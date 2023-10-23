input()
a = tuple( map( int, input().split() ) )
x = int( input() )
p = True

for i in range( len( a ) - 1, -1, -1 ):
    if a[i] == x:
        print( i )
        p = False
        break

if p:
    print( -1 )
