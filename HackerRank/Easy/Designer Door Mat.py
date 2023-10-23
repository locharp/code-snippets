N, M = map( int, input().split() )
width = N * 3
margin = [ ( ".|." * ( i * 2 + 1 ) ).center( width, "-" ) for i in range( N // 2 ) ]
main = "WELCOME".center( width, "-" )
mat = margin + [ main ] + margin[ : : -1 ]

for line in mat:
    print( line )
