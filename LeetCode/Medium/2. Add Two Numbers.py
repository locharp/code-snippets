class Solution:
    def addTwoNumbers( self, l1: Optional[ListNode], l2: Optional[ListNode] ) -> Optional[ListNode]:
        m = 0
        n = 0
        i = 1
        
        while l1 != None:
            m += l1.val * i
            l1 = l1.next
            i *= 10
            
        i = 1
        
        while l2 != None:
            n += l2.val * i
            l2 = l2.next
            i *= 10
            
        i = m + n
        head = curr = ListNode( i % 10 )
        
        while i > 9:
            i //= 10
            curr.next = ListNode( i % 10 )
            curr = curr.next
            
        return head