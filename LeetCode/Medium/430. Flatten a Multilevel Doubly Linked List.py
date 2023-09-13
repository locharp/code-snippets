class Solution:
    def flatten( self, head: 'Optional[Node]' ) -> 'Optional[Node]':
        if head == None:
            return head
        
        curr = Node( 0 )
        q = [ head ]
        
        while len( q ) > 0:
            curr.next = q.pop()
            curr.next.prev = curr
            curr = curr.next
            
            if curr.next != None:
                q.append( curr.next )
                
            if curr.child != None:
                q.append( curr.child )
                curr.child = None
        
        head.prev = None
        return head