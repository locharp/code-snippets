class Solution:
    def hasCycle( self, head: Optional[ListNode] ) -> bool:
        a = set()
        
        while head is not None:
            if head in a:
                return True
            else:
                a.add( head )
                
            head = head.next
            
        return False