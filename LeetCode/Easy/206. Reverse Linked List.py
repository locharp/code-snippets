class Solution:
    def reverseList( self, head: Optional[ListNode] ) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        
        while curr.next is not None:
            head, head.next, curr.next = curr.next, head, curr.next.next
            
        return head