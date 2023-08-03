class Solution:
    def checkIfExist( self, arr: List[int] ) -> bool:
        n = len( arr )
        
        for i in range( n ):
            for j in arr[ i + 1 : ]:
                if arr[i] * 2 == j or j == arr[i] / 2:
                    return True 
                
        return False