def findAddedCharacter( s, t ):
    c = Counter( s )
    d = Counter( t )
    
    for i in d:
        if i not in c or d[i] > c[i]:
            return i 
