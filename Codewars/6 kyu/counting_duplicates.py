from collections import Counter

def duplicate_count( text ):
    c = Counter( text.lower() )
    
    return len( [ i for i in c if c[i] > 1 ] ) 
