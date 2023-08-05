class Trie:
    def __init__( self ):
        self.is_word = False
        self.children = {}
        
    def add_words( self, words ):
        for word in words:
            curr = self
            
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Trie()
                    
                curr = curr.children[ch]
            
            curr.is_word = True
    
class Solution:
    def wordBreak( self, s: str, wordDict: List[str] ) -> bool:
        trie = Trie()
        trie.add_words( wordDict )
        n = len( s )
        p = [ False ] + [ True ] * ( n )
        
        for i in range( n ):
            if p[i] or s[i] not in trie.children:
                continue
            
            curr = trie
            for j in range( i, n ):
                if s[j] not in curr.children:
                    break
                    
                curr = curr.children[ s[j] ]
                    
                if curr.is_word:
                    p[ j + 1 ] = False
            
        return not p[-1]