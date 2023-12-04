import re

symbol_dict = { " && ": " and ", " || ": " or "  }

def symbols_to_word( match ):
    
    return( symbol_dict[ match.group( 0 ) ] )
    
    
    
for i in range( int( input() ) ):
    print( re.sub( r" && | \|\| ", symbols_to_word, input() ) )
