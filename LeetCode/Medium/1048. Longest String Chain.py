class Solution:
    def longestStrChain( self, words: List[str] ) -> int:
        
        def f( x, y ):
            i = j = 0
            
            while i < len( x ):
                if x[i] != y[j]:
                    if i == j:
                        j += 1
                        continue
                    else:
                        return False
                    
                i += 1
                j += 1
                
            return True
        
        d = defaultdict( list )
        e = {}
        m = 1
        
        for word in words:
            e[word] = 1
            d[ len( word )].append( word )
            
        a = sorted( d )
        
        for i in a:
            if i + 1 not in d:
                continue
                
            for p in d[i]:
                for q in d[ i + 1 ]:
                    if f( p, q ):
                        e[q] = max( e[p] + 1, e[q] )
                        m = max( e[q], m )
                        
        return m
