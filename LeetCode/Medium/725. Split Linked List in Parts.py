class Solution:
    def splitListToParts( self, head: Optional[ListNode], k: int ) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        d = [ None ] * 1000
        ans = [ None ] * k
        
        while curr != None:
            d[n] = curr
            n += 1
            curr = curr.next
            
        p, q = divmod( n, k )
        i = 0
        
        for j in range( q ):
            ans[j] = d[i]
            i += p + 1
            d[ i - 1 ].next = None
            
        for j in range( q, min( k, n ) ):
            ans[j] = d[i]
            i += p
            d[ i - 1 ].next = None
            
        return ans