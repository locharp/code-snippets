class Solution:
    def letterCombinations( self, digits: str ) -> List[str]:
        n = len( digits )
        ans = []
        
        if n == 0:
            return ans
        
        letters = [ "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" ]
        nums = list( map( lambda d: int( d )  - 2, digits ) )
        
        def f( c, i ):
            if i == n:
                ans.append( c )
                return
            
            for ch in letters[ nums[i] ]:
                f( c + ch, i + 1 )
        
        f( "", 0 )
        return ans