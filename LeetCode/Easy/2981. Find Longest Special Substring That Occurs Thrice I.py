class Solution:
    
    def maximumLength( self, s: str ) -> int:
        
        n = len( s )
        c = 1
        d = defaultdict( dict )
        e = "s[0]"
        
        for ch in s:
            if ch == e:
                c += 1
            else:
                if e not in d[c]:
                    d[c][e] = 0
                    
                d[c][e] += 1
                c = 1
                e = ch
                
        if e not in d[c]:
            d[c][e] = 0
            
        d[c][ch] += 1
        m = max( d )
        
        for ch in d[m]:
            if d[m][ch] > 2:
                return m
            
        for ch in d[m]:
            if ( d[m][ch] > 1 and m > 2 ) or ch in d[ m - 1 ]:
                return m - 1
            
        if m > 2:
            return m - 2
        elif max( i for i in d[1].values() ) > 2:
            return 1
        else:
            return -1
