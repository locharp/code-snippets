class Solution:
    def replaceElements( self, arr: List[int] ) -> List[int]:
        x = -1
        
        for i in range( len( arr ) - 1, -1, -1 ):
            if arr[i] > x:
                x, arr[i] = arr[i], x
            else:
                arr[i] = x
                
        return arr