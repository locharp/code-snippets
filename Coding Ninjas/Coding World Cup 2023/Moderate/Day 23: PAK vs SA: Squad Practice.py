from collections import Counter

def splitString( k: int, s: str ) -> int:
    
    c = Counter( s )

    return 1 if len( c ) >= k and max( c.values() ) >= k else 0
