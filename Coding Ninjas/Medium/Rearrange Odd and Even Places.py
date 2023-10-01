def oddEvenList( head ):
    o = head
    p = q = head.next
    
    while q is not None and q.next is not None:
        o.next = q.next
        o = o.next
        q.next = o.next
        q = q.next
            
    o.next = p
    
    return head
