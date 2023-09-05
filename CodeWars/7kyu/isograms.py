def is_isogram( string ):
    s = set()
    
    for ch in string.lower():
        if ch in s:
            return False
        else:
            s.add( ch )
            
    return True