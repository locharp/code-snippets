class Node:
    
    def __init__( self, data, next = None ):
        
        self.data = data
        self.next = next
        
        
        
        

def f( a ):
    
    ans = 0
    
    for i in a:
        ans = ans * 10 + i
        
    return ans



def addFirstAndSecondHalf( head ):
    
    if head is None or head.next is None:
        return head
    
    a = []
    
    while head is not None:
        a.append( head )
        head = head.next
        
    m = ( len( a ) + 1 ) // 2 - 1
    n = len( a ) - 1 
    o = 0
    a[m].next = None
    
    for i in range( n - m ):
        a[ m - i  ].data += a[ n - i ].data + o
        
        if a[ m - i ].data > 9:
            a[ m - i ].data %= 10
            o = 1
        else:
            o = 0
        
    if len( a ) % 2 > 0:
        a[0].data += o
        
        if a[0].data > 9:
            a[0].data %= 10
            o = 1
            
    if o > 0:
        head = Node( 1, a[0] )
    else:
        head = a[0]
        
    while head.data < 1 and head.next is not None:
        head = head.next
        
    return head
