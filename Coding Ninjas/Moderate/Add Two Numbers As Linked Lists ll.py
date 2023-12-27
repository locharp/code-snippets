def addTwoLists( first, second ):
    
    p = q = 0

    while first != None:
        p = ( p * 10 ) + first.data
        first = first.next

    while second != None:
        q = ( q * 10 ) + second.data
        second = second.next

    s = str( p + q )
    ans = curr = Node( int( s[0] ) )

    for i in s[ 1 : ]:
        curr.next = Node( int( i ) )
        curr = curr.next

    return ans
