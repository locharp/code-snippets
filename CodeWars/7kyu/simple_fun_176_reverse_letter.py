def reverse_letter( string ):
    return "".join( ch for ch in string if ch in ascii_lowercase )[ : : -1 ]
