Public Module ApproxFloat



    Public Function f( ByVal x As Double ) As Double
    
        Return x /  ( Math.Sqrt( 1 + x ) + 1 )
        
    End Function
    
    

End Module 
