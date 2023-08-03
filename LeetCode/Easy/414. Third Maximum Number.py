class Solution:
    def thirdMax( self, nums: List[int] ) -> int:
        a = [ -2 ** 31 - 1] * 4
        
        for num in nums:
            if num > a[0] and a[2] != num != a[1]:
                if num > a[1]:
                    if num > a[2]:
                        a[2], a[1], a[0] = num, a[2], a[1]
                    else:
                        a[1], a[0] = num, a[1]
                else:
                    a[0] = num
                       
        return a[2] if a[0] == a[3] else a[0]