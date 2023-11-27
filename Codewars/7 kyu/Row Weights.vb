Public Module Kata
    
    
    
  Public Function RowWeights( ByVal array As Integer() ) As Integer()
        
      Dim ans() = { 0, 0 }
        
      For i = 0 To array.getUpperBound( 0 )
          ans( i Mod 2 ) += array( i )
      Next
      
      Return ans
        
  End Function
    
    
    
End Module
