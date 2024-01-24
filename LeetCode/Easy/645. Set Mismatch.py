class Solution:

    def findErrorNums( self, nums: List[int] ) -> List[int]:
        
        c = Counter( nums )

        return [ c.most_common( 1 )[0][0], ( { i for i in range( 1, len( nums ) + 1 ) } - set( c ) ).pop() ]
