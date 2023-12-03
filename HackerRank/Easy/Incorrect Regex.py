import re

a = [ "*+", "++", "?+" ]

for i in range( int( input() ) ):
    try:
        exp = input()
        
        for j in a:
            if j in exp:
                raise re.error( "False" )
                
        re.compile( exp )
        
        print( "True" )
    except re.error:
        print( "False" )
