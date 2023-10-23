input()
a = tuple( map( int, input().split() ) )
x = int( input() )

print( a.index( x ) if x in a else -1 )
