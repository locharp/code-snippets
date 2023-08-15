class Solution:
    def partition( self, head: Optional[ListNode], x: int ) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head.next
        
        if head.val < x:
            g = head
            
            while curr is not None and curr.val < x:
                g.next = curr
                g = curr
                curr = curr.next
                
            h = i = curr
        else:
            h = i = head
            
            while curr is not None and curr.val >= x:
                i.next = curr
                i = curr
                curr = curr.next
                
            head = g = curr
        
        if g is None:
            return h
        elif h is None:
            return head
        
        curr = curr.next
        
        while curr is not None:
            if curr.val < x:
                g.next = curr
                g = curr
            else:
                i.next = curr
                i = curr
            
            curr = curr.next
            
        i.next, g.next = None, h
        
        return head