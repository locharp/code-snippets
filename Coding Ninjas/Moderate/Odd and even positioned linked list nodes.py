def oddEvenLinkedList( head ):
    
    odd = head
    even = head2 = head.next
    
    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        
        if odd.next is not None:
            even.next = odd.next
            even = even.next
        else:
            even.next = None
            
    odd.next = head2
    
    return head
