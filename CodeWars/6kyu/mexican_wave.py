def wave( people ):
    n = len( people )
    ans = []
    
    for i in range( n ):
        if people[i] == " ":
            continue
        
        s = ""
        for j in range( n ):
            if j == i:
                s += people[j].upper()
            else:
                s += people[j]
                
        ans.append( s )
        
    return ans