from re import compile, match

pattern = compile( "^[789]\d{9}$" )

for i in range( int( input() ) ):
    print( "YES" if pattern.match( input() ) != None else "NO" )
