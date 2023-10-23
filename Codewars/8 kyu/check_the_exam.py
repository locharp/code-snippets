def check_exam( arr1,arr2 ):
    ans = 0
    
    for i in range( len( arr1 ) ):
        if arr1[i] == arr2[i]:
            ans += 4
        elif arr2[i] != "":
            ans -= 1
            
    return max( ans, 0 )
