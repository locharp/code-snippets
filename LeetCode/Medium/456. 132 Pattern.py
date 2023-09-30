class Solution:
    def __init__( self ):
        self.d = []
        
    def find132pattern( self, nums: List[int] ) -> bool:
        if len( nums ) < 1:
            return False
            
        o = nums.pop( 0 )
        i = len( self.d ) - 1
        
        while i >= 0:
            if self.d[i][0] < o:
                t = False
                
                if len( self.d[i] ) > 1:
                    if self.d[i][1] > o:
                        return True
                    else:
                        self.d[i][1] = o
                else:
                    self.d[i].append( o )
                    
                i -= 1
                
                while i > 0:
                    if self.d[i][0] < o and ( len( self.d[i] ) < 2 or self.d[i][1] <= o ):
                        self.d.pop( i )
                        i -= 1
                    else:
                        break
            else:
                break
                    
        if i == len( self.d ) - 1:
            self.d.append( [ o ] )
            
        return self.find132pattern( nums )
