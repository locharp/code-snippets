class Solution:
    def getIntersectionNode( self, headA: ListNode, headB: ListNode ) -> Optional[ListNode]:
        a = set()
        
        while headA != None:
            a.add( headA )
            headA = headA.next
            
        while headB != None:
            if headB in a:
                return headB
            
            headB = headB.next
            
        return None