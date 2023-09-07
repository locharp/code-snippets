class Solution:
    def reverseBetween( self, head: Optional[ListNode], left: int, right: int ) -> Optional[ListNode]:
        if left == right:
            return head
            
        i = right - left
        a = [ 0 ] * ( i + 1 )
        curr = head
        
        for j in range( left - 1 ):
            curr = curr.next
            
        left = curr
        for j in range( i, -1, -1 ):
            a[j] = curr.val
            curr = curr.next
            
        for j in a:
            left.val = j
            left = left.next
            
        return head