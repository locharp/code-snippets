def findSubmatrixSum( arr, queries ):
    
    for i in arr:
        for j in range( 1, len( i ) ):
            i[j] += i[ j - 1 ]

    ans = []
    
    for p, q, r, s in queries:
        ans.append( 0 )

        for i in arr[ p : r + 1 ]:
            if q < 1:
                ans[-1] += i[s]
            else:
                ans[-1] += i[s] - i[ q - 1 ]
        
    return ans
