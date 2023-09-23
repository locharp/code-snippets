def findNonRepeating( str ):
    d = {}
    c = []
    
    for ch in str:
        if ch not in d:
            d[ch] = 0
            c.append( ch )
            
        d[ch] += 1
        
    for ch in c:
        if d[ch] == 1:
            return ch
        
    return "#"
