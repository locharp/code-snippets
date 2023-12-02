import os
from datetime import datetime

def time_delta( t1, t2 ):
    
    p = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime( t1, p )
    t2 = datetime.strptime( t2, p )
    td = abs( t1 - t2 )
    ans = int( td.total_seconds() )
    
    return str( ans )
