from datetime import *

def unlucky_days( year ):
    
    ans = 0
    
    for i in range( 1, 12 ):
        if date( year, i, 13 ).weekday() == 4:
            ans += 1
            
    return ans
