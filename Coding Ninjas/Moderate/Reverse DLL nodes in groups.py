def reverseDLLInGroups( head, k ):
    if head.next is None or k == 1:
        return head
    
    
    
    def f( h, i, k, p, q, ans ):
        
        if i % k == 0 and h.next is not None:
            q.next = h.next
            h.next.prev = q
            h.next = h.prev
            h.prev = p
            
            if p is not None:
                p.next = h
                
            if i == k:
                ans.append( h )
                
            if q.next.next is not None:
                f( q.next.next, i + 2, k, q, q.next, ans )
        elif h.next is None:
            if p is not None:
                p.next = h
            
            h.next = h.prev
            h.prev = p
            q.next = None
            
            if i <= k:
                ans.append( h )
        else:
            h.prev, h.next = h.next, h.prev
            f( h.prev, i + 1, k, p, q, ans )

  
    
    ans = []
    f( head.next, 2, k, None, head, ans )
    
    return ans.pop()
