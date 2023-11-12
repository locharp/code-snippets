class Solution:
  
    def minOperations( self, nums1: List[int], nums2: List[int] ) -> int:
        
        m = len( nums1 )
        n = len( nums2 )
        p = 0
        q = 1
        
        for i in range( len( nums1 ) - 1 ):
            if nums1[i] > nums1[-1] or nums2[i] > nums2[-1]:
                if nums1[i] > nums2[-1] or nums2[i] > nums1[-1]:
                    return -1
                else:
                    p += 1
                    
            if nums1[i] > nums2[-1] or nums2[i] > nums1[-1]:
                q += 1
                
        return min( p, q )
