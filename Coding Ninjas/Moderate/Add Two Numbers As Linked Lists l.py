def addTwoLists(first, second):
    num1 = num2 = 0
    
    while first is not None:
        num1 = num1 * 10 + first.data
        first = first.next
        
    while second is not None:
        num2 = num2 * 10 + second.data
        second = second.next
    
    total = num1 + num2
    head = Node( total % 10 )
    
    while total > 9:
        total //= 10
        tail = head
        head = Node( total % 10 )
        head.next = tail
        
    return head