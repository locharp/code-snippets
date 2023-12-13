import re

pattern = re.compile( r"(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$" )

for i in range( int( input() ) ):
    if pattern.match( input() ) != None:
        print( "Valid" )
    else:
        print( "Invalid" )
