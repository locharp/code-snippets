from typing import List

def happyPlayers( balls : List[int] ) -> int:
    
    c = set()
    d = set()
    
    for ball in balls:
        if ball in c:
            d.add( ball )
        else:
            c.add( ball )
            
    if len( d ) > 0:
        return max( d )
    else:
        return -1
