class Trie:

    def __init__( self ):
        self.trie = defaultdict( Trie )
        self.is_word = False

    def insert( self, word: str ) -> None:
        p = self
        
        for ch in word:
            if ch not in p.trie:
                p.trie[ch] = Trie()
                
            p = p.trie[ch]
        
        p.is_word = True

    def search( self, word: str,) -> bool:
        p = self
        
        for ch in word:
            if ch in p.trie:
                p = p.trie[ch]
            else:
                return False
                
        return p.is_word

    def startsWith(self, prefix: str) -> bool:
        p = self
        
        for ch in prefix:
            if ch in p.trie:
                p = p.trie[ch]
            else:
                return False
            
        return True