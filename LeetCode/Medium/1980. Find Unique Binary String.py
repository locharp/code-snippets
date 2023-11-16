class Solution:
    
    def findDifferentBinaryString( self, nums: List[str] ) -> str:
        
        a = [ int( i, 2 ) for i in nums ]
        s = { i for i in range( len( nums ) + 1 ) }
        
        for i in s.difference( a ):
            return bin( i )[ 2 : ].zfill( len( nums ) )
