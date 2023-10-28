from collections import *

def splitString( string: str ) -> bool:

    a = "aeiou"
    n = len( string ) // 2
    p = sum( j for i, j in Counter( string[ : n ].lower() ).items() if i in a )
    q = sum( j for i, j in Counter( string[ n : ].lower() ).items() if i in a )

    return p == q
