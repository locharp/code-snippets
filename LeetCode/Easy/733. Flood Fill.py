class Solution:
    
    def floodFill( self, image: List[ List[int] ], sr: int, sc: int, color: int ) -> List[ List[int] ]:
        
        if image[sr][sc] == color:
            return image
        
        o = image[sr][sc]
        image[sr][sc] = color
        
        for i, j in [ [ -1, 0 ], [ 0, -1 ], [ 0, 1 ], [ 1, 0 ] ]:
            p, q = sr + i, sc + j
            
            if p < 0 or p == len( image ) or q < 0 or q == len( image[0] ):
                continue
                
            if image[p][q] == o:
                self.floodFill( image, p, q, color )
                
        return image
