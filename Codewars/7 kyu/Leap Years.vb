Module Kata
    
    
    
    Public Function IsLeapYear( year As Integer ) As Boolean
        
        Return year Mod 4 = 0 And ( year Mod 100 > 0 Or year Mod 400 = 0 )
        
    End Function
    
    
    
End Module
