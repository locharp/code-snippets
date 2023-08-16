class Solution:
    def mergeTwoLists( self, list1: Optional[ListNode], list2: Optional[ListNode] ) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val > list2.val:
            list1, list2 = list2, list1
            
        curr = list1
            
        while list2:
            while curr.next and curr.next.val <= list2.val:
                curr = curr.next
                
            curr.next, list2 = list2, curr.next
            
        return list1