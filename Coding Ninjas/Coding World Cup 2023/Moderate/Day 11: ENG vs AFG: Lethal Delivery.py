from math import *

def maximumSquareDivisor( n: int ) -> int:
    
    for i in range( floor( sqrt( n ) ), 0, -1 ):
        if n % i ** 2 == 0:
            return i
