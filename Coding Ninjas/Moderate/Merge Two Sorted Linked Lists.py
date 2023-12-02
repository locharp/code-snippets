def sortTwoLists( first, second ):
    
    curr = head = Node( 0 )

    while first != None and second != None:
        if first.data > second.data:
            curr.next = second
            second = second.next
        else:
            curr.next = first
            first = first.next

        curr = curr.next

    if first != None:
        curr.next = first
    elif second != None:
        curr.next = second
        
    return head.next
