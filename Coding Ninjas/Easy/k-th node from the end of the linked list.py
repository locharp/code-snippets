def findKthFromLast( head, k ):
    
    ans = head

    for i in range( k ):
        head = head.next

    while head != None:
        head = head.next
        ans = ans.next

    return ans
