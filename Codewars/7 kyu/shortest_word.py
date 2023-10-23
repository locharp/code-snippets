def find_short( s ):
    return sorted( map( len, s.split() ) )[0]