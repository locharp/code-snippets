from typing import *

def bitwise_inclusion( n: int, a: List[int] ) -> int:
    
    ans = 0

    for i in range( n ):
        j = i + 1
        k = a[i]
        
        while j < n:
            k &= a[j]

            if k < 1:
                break

            j += 1

        ans += ( j - i ) * a[i]
        
    return ans

for i in range( int( input() ) ):
    print( bitwise_inclusion( int( input() ), [ int( j ) for j in input().split() ] ))
