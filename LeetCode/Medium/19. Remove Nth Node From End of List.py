class Solution:
    def removeNthFromEnd( self, head: Optional[ListNode], n: int ) -> Optional[ListNode]:
        target = curr = head
        i = n
        
        while i > 0 and curr.next is not None:
            curr = curr.next
            i -= 1
        
        if i > 0:
            return head.next
        
        while curr.next is not None:
            target = target.next
            curr = curr.next
            
        if n == 1:
            target.next = None
        else:
            target.next = target.next.next
            
        return head