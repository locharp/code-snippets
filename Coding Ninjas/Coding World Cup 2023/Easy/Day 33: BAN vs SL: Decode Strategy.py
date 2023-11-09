def decodeString( s: str ) -> str:
    
    return "".join( chr( ( ord( i ) - 96 ) % 26 + 97 ) for i in s )
