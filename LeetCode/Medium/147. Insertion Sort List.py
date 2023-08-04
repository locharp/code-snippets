class Solution:
    def insertionSortList( self, head: Optional[ListNode] ) -> Optional[ListNode]:
        curr = head
        
        while curr.next is not None:
            if curr.next.val < curr.val:
                pos = head
                
                if curr.next.val < pos.val:
                    curr.next.next, head, curr.next = pos, curr.next, curr.next.next
                else:
                    while pos.next is not None and curr.next.val > pos.next.val:
                        pos = pos.next
                    
                    curr.next.next, pos.next, curr.next = pos.next, curr.next, curr.next.next
                    
            else:
                curr = curr.next
                    
        return head