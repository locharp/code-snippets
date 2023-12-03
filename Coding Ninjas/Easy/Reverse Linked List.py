def reverseLinkedList( head ):

    if head == None or head.next == None:
        return head
        
    curr = head.next
    head.next = None
    
    while curr != None:
        temp = curr.next
        curr.next = head
        head = curr
        curr = temp

    return head
