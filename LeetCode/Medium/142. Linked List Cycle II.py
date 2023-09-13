class Solution:
    def detectCycle( self, head: Optional[ListNode] ) -> Optional[ListNode]:
        a = set()
        
        while head != None:
            if head in a:
                break
                
            a.add( head )
            head = head.next
            
        return head