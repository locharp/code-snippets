s = "".join( matrix[i][j] for j in range( m ) for i in range( n ) )
ans = re.sub( "(?<=\w)\W+(?=\w)", " ", s )

print( ans )
