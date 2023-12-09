# Following is the class structure of the Node class:
class Node:

    def __init__( self, data ):

        self.data = data
        self.next = None



def addFirstAndReversedSecondHalf(head):
    
    if head == None or head.next == None:
        return head
        
    m = []
    n = []
    p = q = head
    
    while q != None:
        m.append( p.data )
        p = p.next
        q = q.next

        if q != None:
            q = q.next

    while p != None:
        n.append( p. data )
        p = p.next

    n.reverse()
    o = max( len( m ), len( n ) ) + 1
    arr = [ 0 ] * o
    i = -1
    
    if len( m ) < len( n ):
        m, n = n, m

    while i >= -len( n ):
        p, q = divmod( m[i] + n[i], 10 )
        arr[i] += q
        arr[ i - 1 ] += p
        i -= 1

    while i >= -len( m ):
        arr[i] += m[i]

        if arr[i] > 9:
            arr[i] %= 10
            i -= 1
            arr[i] += 1
        else:
            i -= 1

    ans = curr = Node( arr[0] )
    
    for i in arr[ 1 : ]:
        curr.next = Node( i )
        curr = curr.next

    while ans.data < 1 and ans.next != None:
        ans = ans.next

    return ans
