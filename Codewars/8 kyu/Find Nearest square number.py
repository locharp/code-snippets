from math import *

def nearest_sq( n ):
    
    o = floor( sqrt( n ) )
    p = pow( o, 2 )
    q = pow( o + 1, 2 )
    
    if q - n > n - p:
        return p
    else:
        return q
