class Solution:
    def validMountainArray( self, arr: List[int] ) -> bool:
        n = len( arr ) - 1
        i = 0
        
        while i < n and arr[i] < arr[ i + 1 ]:
            i += 1
            
        if i == 0 or i == n:
            return False
        
        while i < n and arr[i] > arr[ i + 1 ]:
            i += 1
            
        return i == n