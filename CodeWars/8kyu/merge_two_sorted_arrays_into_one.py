def merge_arrays( arr1, arr2 ):
    arr1.sort()
    arr2.sort()
    ans = []
    i = j = 0
    m = len( arr1 )
    n = len( arr2 )

    while i < m:
        if arr1[i] >= arr2[j]:
            ans.append( arr2[j] )
            
            if arr1[i] == arr2[j]:
                i += 1
                
            j +=1
            
            if j >= n:
                break
        else:
            ans.append( arr1[i] )
            i += 1
            
    return ans + arr1[ i : ] + arr2[ j : ]
