class Trie:
    def __init__( self ):
        self.children = {}
        self.is_word = False
        
    def add_word( self, word ):
        curr = self
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
                
            curr = curr.children[ch]
        
        curr.is_word = True
        
    def find( self, word ):
        curr = self
        
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
            
        return curr.is_word
        
class Solution:
    def minExtraChar( self, s: str, dictionary: List[str] ) -> int:
        trie = Trie()
        n = len( s )
        ans = [ 0 ] * ( n + 1 )
        
        for word in dictionary:
            trie.add_word( word )
            
        for i in range( n - 1, -1, -1 ):
            ans[i] = ans[ i + 1 ] + 1
            
            for j in range( i + 1, n + 1 ):
                if trie.find( s[ i : j ] ):
                    ans[i] = min( ans[i], ans[j] )
                    
        return ans[0]