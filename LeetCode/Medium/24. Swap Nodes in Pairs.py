class Solution:
    def swapPairs( self, head: Optional[ListNode] ) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        m = head
        head = m.next
        m.next = head.next
        head.next = m
        n = m.next
        
        while n != None and n.next != None:
            n = n.next
            m.next.next = n.next
            n.next = m.next
            m.next = n
            m = n.next
            n = m.next
            
        return head