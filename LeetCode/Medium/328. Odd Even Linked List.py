class Solution:
    def oddEvenList( self, head: Optional[ListNode] ) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        o, e, c = [], [], 1
        
        curr = head
        
        while curr is not None:
            o.append( curr.val ) if c % 2 == 1 else e.append( curr.val )
            curr = curr.next
            c += 1
            
        o += e
        head.val = o.pop( 0 )
        curr = head.next
        
        for i in o:
            curr.val = i
            curr = curr.next
            
        return head