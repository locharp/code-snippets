from typing import List

def f( arr, k, m, i ):

    p = m

    for j in range( i, len( arr ) ):
        if m + arr[j] > k:
            continue
        elif m + arr[j] == k:
            return k
        
        q = f( arr, k, m + arr[j], j + 1 )

        if q > p:
            p = q

    return p

        

def kSumSubset ( arr: List[int], k: int ) -> int:
    
    arr = sorted( [ i for i in arr if i <= k ], reverse = True )
    ans = f( arr, k, 0, 0 )

    return ans
