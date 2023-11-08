def evaporator( content, evap_per_day, threshold ):
    
    evap_per_day = ( 100 - evap_per_day ) / 100
    ans = 0
    threshold  /= 100
    p = 1
    
    while p >= threshold:
        ans += 1
        p *= evap_per_day
        
    return ans
