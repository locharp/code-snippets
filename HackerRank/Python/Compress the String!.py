from itertools import groupby

print( " ".join( [ f"({ len( list( x ) ) }, {c})" for c, x in groupby( map( int, input() ) ) ] ) )
