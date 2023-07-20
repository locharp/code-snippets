class Solution:
    def merge( self, nums1: List[int], m: int, nums2: List[int], n: int ) -> None:
        m -= 1
        o = m + n
        n -= 1
        
        while m >= 0 and n >= 0:
            if nums2[n] >= nums1[m]:
                nums1[o] = nums2[n]
                n -= 1
            else:
                nums1[o] = nums1[m]
                m -= 1
            
            o -= 1
                
        for i in range( n, -1, -1 ):
            nums1[o] = nums2[i]
            o -= 1