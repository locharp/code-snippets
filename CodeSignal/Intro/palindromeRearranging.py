from collections import Counter

def solution( inputString ):
    c = Counter( inputString )

    return sum( i % 2 for i in c.values() ) < 2