class Solution:
    def removeElements( self, head: Optional[ListNode], val: int ) -> Optional[ListNode]:
        while head != None and head.val == val:
            head = head.next
            
        if head == None:
            return head
        
        curr = head
        
        while curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head