Public Module Histo
    
    
    
    Public Function Hist( ByVal s As String ) As String
        
        Dim d = New Dictionary( Of String, Integer ) From { { "u", 0 }, { "w", 0 }, { "x", 0 }, { "z", 0 } }
        Dim ans = ""
        
        For Each ch in s
            If d.ContainsKey( ch )
                d( ch ) += 1
            End If
        Next
        
        For Each item in d
            If item.Value = 0
                Continue For
            End If
            
            ans &= item.Key.PadRight( 3 ) & item.Value.ToString().PadRight( 6 ) & New String( "*", item.Value ) & "\r"
        Next
        
        If ans.Length < 3
            Return ans
        Else
            Return ans.Remove( ans.Length - 2 )
        End If
        
    End Function
    
    
    
End Module
