from collections import Counter

def find_it( seq ):
    
    c = Counter( seq )
    
    for i,j in c.items():
        if j % 2 == 1:
            return i
