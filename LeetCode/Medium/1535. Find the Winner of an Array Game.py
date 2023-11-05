class Solution:
    
    def getWinner( self, arr: List[int], k: int ) -> int:
        
        n, o = 0, arr[0]
        
        for i in arr[ 1 : ]:
            if i > o:
                o = i
                n = 1
            else:
                n += 1
                
            if n == k:
                break
            
        return o
