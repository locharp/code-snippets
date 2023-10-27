def alphabet_position( text ):
    
    return " ".join( str( ord( ch ) - 64 ) for ch in text.upper() if ch.isalpha() )
