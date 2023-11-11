from typing import List

def f( a, d, i, j, o ):
  
    ans = 0
  
    for p, q in d:
        r, s = i + p, j + q
        
        if r >= 0 and r < len( a ) and s >= 0 and s < len( a[0] ):
            if a[r][s] == 2:
                if o == 0:
                    ans += 1
            elif a[r][s] == 0:
                a[r][s] = -1
                ans += f( a, d, r, s, o - 1 )
                a[r][s] = 0
                
    return ans



def robotPaths( n: int, m: int, arr: List[ List[int] ] ) -> int:
    
    o = p = q = 0
    d = ( ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ) )
    
    for i in range( n ):
        for j in range( m ):
            if arr[i][j] == 0:
                o += 1
            elif arr[i][j] == 1:
                p = i
                q = j
                
    return f( arr, d, p, q, o )
