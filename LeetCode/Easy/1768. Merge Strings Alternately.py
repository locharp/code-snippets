class Solution:
    def mergeAlternately( self, word1: str, word2: str ) -> str:
        n = min( len( word1 ), len( word2 ) )
        ans = ""
        
        for i in range( n ):
            ans += word1[i] + word2[i]
            
        ans += word1[ n : ] + word2[ n : ]
        
        return ans