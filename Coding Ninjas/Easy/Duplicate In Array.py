
def findDuplicate( arr ):
    s = set()
    
    for i in arr:
        if i in s:
            return i
        
        s.add( i )