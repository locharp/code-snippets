class Solution:
    def duplicateZeros( self, arr: List[int] ) -> None:
        n = len( arr )
        i = n + arr.count( 0 ) - 1
        j = n - 1
        
        while j >= 0:
            if i < n:
                if arr[j] == 0:
                    arr[i] = 0
                    i -= 1
                arr[i] = arr[j]
            elif i == n:
                if arr[j] == 0:
                    i -= 1
                    arr[i] = 0
            else:
                if arr[j] == 0:
                    i -= 1
                    
            i -= 1
            j -= 1