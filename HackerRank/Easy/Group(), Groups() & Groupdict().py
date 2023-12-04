import re

match = re.search( r"(\w(?!_))\1", input() )

if match is None:
    print( -1 )
else:
    print( match.group( 0 )[0] )
