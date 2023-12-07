import re


pattern = re.compile( r"(#(?:[a-fA-F0-9]{3}){1,2})[),;]" )

for i in range( int( input() ) ):
    a = re.findall( pattern, input() )
    
    if a != None:
        for i in a:
            print( i )
