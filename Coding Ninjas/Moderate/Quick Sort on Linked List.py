def quickSortLL( head ):
    a = []
    curr = head
    
    while curr is not None:
        a.append( curr.data )
        curr = curr.next
        
    a.sort()
    curr = head
    
    for i in a:
        curr.data = i
        curr = curr.next
        
    return head