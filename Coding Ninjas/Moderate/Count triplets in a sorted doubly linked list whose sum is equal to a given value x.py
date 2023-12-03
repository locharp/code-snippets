def countTriplets( head, x, n = 0 ):
    
    if n > 2:
        return 1 if x == 0 else 0
    elif head == None or x - head.data < 0:
        return -1
    
    ans = 0
    curr = head
    y = x
    
    while curr != None and y > 0:
        y = x - curr.data
        t = countTriplets( curr.next, x - curr.data, n + 1 )
        
        if t < 0:
            break
        elif t > 0:
            ans += t
            
        curr = curr.next
        
    return ans
