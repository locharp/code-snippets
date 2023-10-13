def quick_sort( head ):
    
    prev = next = head
    curr = head.next
    
    while curr is not None:
        temp = curr.next
        
        if curr.value > head.value:
            next.next = curr
            curr.prev = next
            next = curr
        else:
            prev.prev = curr
            curr.next = prev
            prev = curr
            
        prev.prev = next.next = None
        curr = temp
        
    if next is not head:
        n = quick_sort( head.next )
        n[0].prev = head
        head.next = n[0]
        next = n[1]
        
    if prev is not head:
        head.prev.next = None
        m = quick_sort( prev )
        m[1].next = head
        head.prev = m[1]
        prev = m[0]
        
    return ( prev, next )



def quickSort( head ):
    
    return quick_sort( head )[0]
