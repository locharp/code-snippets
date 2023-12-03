Public Module Rotations
    
    
    
    Public Function ContainAllRots( ByVal s As String, ByVal arr As List( Of String ) ) As Boolean
        
        For i = 0 To s.Length - 1
            If Not arr.Contains( s.Substring( i ) & s.Substring( 0, i ) )
                Return False
            End If
        Next
        
        Return True
        
    End Function
    
    
    
End Module
