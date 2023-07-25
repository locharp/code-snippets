def number( bus_stops ):
    ans = 0
    
    for x, y in bus_stops:
        ans += x - y
        
    return ans