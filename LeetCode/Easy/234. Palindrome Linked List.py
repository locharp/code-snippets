class Solution:
    def isPalindrome( self, head: Optional[ListNode] ) -> bool:
        a = []
        
        while head is not None:
            a.append( head.val )
            head = head.next
        
        n = len( a )
        
        return a[ : n // 2 ] == a[ -1 : ( n - 1 ) // 2 : -1 ]