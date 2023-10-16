from collections import defaultdict

def delete_nth( order, max_e ):
    ans = []
    d = defaultdict( int )
    
    for i in order:
        d[i] += 1
        
        if d[i] <= max_e:
            ans.append( i )
            
    return ans
