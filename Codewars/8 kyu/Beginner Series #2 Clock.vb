Public Module Kata



    Public Function Past( ByVal h As Integer, ByVal m As Integer, ByVal s As Integer ) As Integer
        
        Return ( ( ( ( h * 60 ) + m ) * 60 ) + s ) * 1000
        
    End Function
    
    
    
End Module
