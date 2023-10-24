from typing import List

def f( a, n, s ):
    
    if len( s ) == n:
        a.append( s )
    elif len( s ) > n:
        return

    f( a, n, s + "0" )

    if len( s ) < 1 or s[-1] != "1":
        f( a, n, s + "1" )



def generateString( N: int ) -> List[str]:

    ans = []
    f( ans, N, "" )

    return ans
