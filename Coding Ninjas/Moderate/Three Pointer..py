def threePointer( X:list, Y:list, Z:list ):
    
    ans = 2147483647
    a, b, c = len( X ) - 1, len( Y ) - 1, len( Z ) - 1
    i = j = k = 0
    
    while len( X ) != i and len( Y ) != j and len( Z ) != k:
    
        if X[i] > Y[j]:
            if X[i] > Z[k]:
                if Y[j] > Z[k]:
                    ans = min( ans, X[i] - Z[k] )
                    
                    if k < c:
                        k += 1
                    else:
                        break
                else:
                    ans = min( ans, X[i] - Y[j] )
                    
                    if j < b:
                        j += 1
                    else:
                        break
            else:
                ans = min( ans, Z[k] - Y[j] )
                
                if j < b:
                    j += 1
                else:
                    break
        elif X[i] > Z[k]:
            ans = min( ans, Y[j] - Z[k] )
            
            if k < c:
                k += 1
            else:
                break
        else:
            if Y[j] > Z[k]:
                ans = min( ans, Y[j] - X[i] )
            else:
                ans = min( ans, Z[k] - X[i] )
                
            if i < a:
                i += 1
            else:
                break
                
    return ans
