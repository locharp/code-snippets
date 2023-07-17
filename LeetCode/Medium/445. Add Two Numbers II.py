class Solution:
    def addTwoNumbers( self, l1: Optional[ListNode], l2: Optional[ListNode] ) -> Optional[ListNode]:
        x = y = 0
        
        while l1 is not None:
            x = x * 10 + l1.val
            l1 = l1.next
            
        while l2 is not None:
            y = y * 10 + l2.val
            l2 = l2.next
            
        x += y
        
        if x == 0:
            return ListNode( 0 )
        
        ans = None
        while x > 0:
            x, y = divmod( x, 10 )
            ans = ListNode( y, ans )
            
        return ans