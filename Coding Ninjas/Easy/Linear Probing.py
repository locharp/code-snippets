def linearProbing( keys ):
    
    n = len( keys )
    ans = [ -1 ] * n
    
    for i in keys:
        j = i % n
        
        if ans[j] < 0:
            ans[j] = i
        else:
            t = True

            for k in range( j + 1, n ):
                if ans[k] < 0:
                    ans[k] = i
                    t = False
                    break

            if t:
                for k in range( j ):
                    if ans[k] < 0:
                        ans[k] = i
                        break

    return ans
