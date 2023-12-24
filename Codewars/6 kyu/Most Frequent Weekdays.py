from calendar import *

def most_frequent_days( year ):
    
    ans = [ weekday( year, 1, 1 ) ]
    
    if isleap( year ):
        ans.append( weekday( year, 1, 2 ) )
        
    return [ day_name[i] for i in sorted( ans ) ]
