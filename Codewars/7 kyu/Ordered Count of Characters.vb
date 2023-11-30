Public Module Kata
    
    
    
    Public Function OrderedCount( input as String ) As List( Of Tuple( Of Char, Integer ) )
        
        Dim ans = New List( Of Tuple( Of Char, Integer ) )
        Dim a = From ch In input
            Group By ch
            Into Count
            
        For Each g In a
            ans.Add( Tuple.Create( g.ch, g.Count ) )
        Next
    
        Return ans
        
    End Function



End Module




' 2
Public Module Kata
    
    
    
    Public Function OrderedCount( input as String ) As List( Of Tuple( Of Char, Integer ) )
        
        Dim d = New Dictionary( Of Char, Integer )
        Dim ans = New List( Of Tuple( Of Char, Integer ) )
        
        For Each ch In input
            If d.ContainsKey( ch )
                d( ch ) += 1
            Else
                d( ch ) = 1
            End If
        Next
        
        For Each item in d
            ans.Add( New Tuple( Of Char, Integer )( item.Key, item.Value ) )
        Next
        
        Return ans
        
    End Function
    
    
    
End Module





' 3
Public Module Kata
    
    
    
    Public Function OrderedCount(input as String) As List(Of Tuple(Of Char, Integer))
        
        Return input.
            GroupBy( Function( x ) x).
            Select( Function( x ) _
                Tuple.Create( x.Key, x.Count ) ).
            ToList()
                        
    End Function
                
                
                
End Module
