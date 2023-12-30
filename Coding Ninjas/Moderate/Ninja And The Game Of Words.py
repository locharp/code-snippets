from collections import Counter

def getFrequency( str, words, n ):
    
    c = Counter( str.split() )
    
    return [ c[i] for i in words ]
