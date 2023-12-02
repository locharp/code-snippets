class Solution:

    def countCharacters( self, words: List[str], chars: str ) -> int:
        
        c = Counter( chars )
        
        return sum( len( word ) for word in words if len( Counter( word ) - c ) < 1 )
