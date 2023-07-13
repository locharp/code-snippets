class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min( map( len, strs ) )
        
        for s in strs[1:]:
            for i in range( n ):
                if s[i] != strs[0][i]:
                    strs[0] = s[:i]
                    n = i
                    break
            
            if len( strs[0] ) == 0:
                return ""
                
        return strs[0][:n]