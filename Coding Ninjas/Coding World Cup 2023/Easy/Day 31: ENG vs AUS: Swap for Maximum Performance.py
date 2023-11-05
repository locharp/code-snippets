def maxSwap( a: List[int] ) -> int:
    
    if a[0] > a[-1]:
        return a[0] + max( a[ 1 : ] )
    else:
        return a[-1] + max( a[ : -1 ] )
