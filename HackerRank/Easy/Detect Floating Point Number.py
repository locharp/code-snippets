import re

pattern = re.compile( r"[\+|-]?\d*\.\d+$" )

for i in range( int( input() ) ):
    print( pattern.match( input() ) != None )
