' Either the expected of the actual becomes <string.Empty> for unknow reasons.

Public Module ApproxInter
    
    Public Function Interp( ByVal f As Func( Of Double, Double ), ByVal l As Double, ByVal u As Double, ByVal n As Integer ) As List( Of Double )
        
        Dim answer = New List( Of Double )()
        Dim d = ( u - l ) / n
        
        For i = 0 To n - 1
            Dim temp = f( l + i * d ) * 100
            temp = Math.Floor( temp ) / 100
            answer.append( temp )
        Next
        
        Return answer
        
    End Function
    
End Module
