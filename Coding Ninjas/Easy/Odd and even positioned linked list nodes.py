def oddEvenLinkedList(head):
    first = head
    h2 = second = head.next
    
    while second is not None and second.next is not None:
        first.next = second.next
        first = first.next
        second.next= second.next.next
        second = second.next
        
    first.next = h2
    
    return head