class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter( s )
        
        for k, v in d.items():
            if v == 1:
                return s.index( k )
            
        return -1