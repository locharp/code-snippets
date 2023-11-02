from math import *

def find_next_square( sq ):
    
    sq = sqrt( sq )
    
    return floor( pow( sq + 1, 2 ) ) if sq.is_integer() else -1
