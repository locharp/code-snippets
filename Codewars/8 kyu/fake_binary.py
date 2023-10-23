def fake_bin( x ):
    return "".join( "0" if ord( ch ) < ord( "5" ) else "1" for ch in x )