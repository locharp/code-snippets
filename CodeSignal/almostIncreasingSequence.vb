Function solution( sequence As List( Of Integer ) ) As Boolean 

Dim Protection = 1
Dim last = sequence.item( 0 )
Dim curr

For i = 1 To sequence.Count - 1
    curr = sequence.Item(i)
    
    If curr <= last Then
        
        If Protection > 0 Then
            Protection -= 1
        Else
            Return False
        End If
        
        If i = 1 Then
            last = curr
        Else If curr > sequence.Item( i - 2 ) Then
            last = curr
        End If
        
    Else
        last = curr
    End If
    
NEXT i

Return True

End Function
