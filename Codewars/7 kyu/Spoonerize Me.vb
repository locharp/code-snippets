Module ReadySet



    Function Spoonerize( ByVal str As String ) As String
    
        Dim a = str.Split()
        Dim ans = a( 1 )( 0 ) & a( 0 ).Substring( 1 ) & " " & a( 0 )( 0 ) & a( 1 ).Substring( 1 )
        
        Return ans
        
    End Function
    
    
    
End Module
