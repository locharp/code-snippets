import re

def symbol_to_word( match ):
    
    if match.group( 0 ) == "&&":
        return "and"
    else:
        return "or"
    
    
    
for i in range( int( input() ) ):
    print( re.sub( "(?<= )(&&|\|\|)(?= )", symbol_to_word, input() ) )
