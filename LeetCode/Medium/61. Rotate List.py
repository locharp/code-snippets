class Solution:
    def rotateRight( self, head: Optional[ListNode], k: int ) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        a = []
        
        while head != None:
            a.append( head )
            head = head.next
            
        k = -( k % len( a ) )
        
        a[-1].next = a[0]
        a[ k - 1 ].next = None
        
        return a[k]