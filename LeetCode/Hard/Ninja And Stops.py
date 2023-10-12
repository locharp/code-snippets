from heapq import heappop, heappush

def minRefuelStops( target, startFuel, stations ):
    q = []
    i = 0
    
    while startFuel < target:
        while i < len( stations ) and startFuel >= stations[i][0]:
            heappush( q, -stations[i][1] )
            i += 1
            
        if len( q ) < 1:
            return -1
        
        startFuel -= heappop( q )
        
    return i - len( q )
