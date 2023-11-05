def isPossible( s: str ) -> int:
    
    return 1 if len( [ i for i in s if i in "aeiou" ] ) >= ( len( s ) + 1 ) // 2 else 0
