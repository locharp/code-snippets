from math import *

def find_next_square( sq ):
    
    sq = sqrt( sq )
    
    if sq.is_integer():
        return floor( pow( sq + 1, 2 ) )
    else:
        return -1
