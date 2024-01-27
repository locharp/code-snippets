Imports System

Public Module Operarray
    
    Public Function gcdi( ByVal x As Long, ByVal y As Long ) As Long
        
        If x = 0 Then
            Return y
        End If
        
        Return Math.Abs( gcdi( y Mod x, x  ) )
        
    End Function
    
    
    
    Public Function lcmu( ByVal a As Long, ByVal b As Long ) As Long
        
        Dim c = gcdi( a, b )
        
        Return Math.Abs( ( a \ c ) * ( b \ c ) * c )
        
    End Function
    
    
    
    Public Function som( ByVal a As Long, ByVal b As Long ) As Long
        
        Return a + b
        
    End Function
    
    
    
    Public Function maxi( ByVal a As Long, ByVal b As Long ) As Long
        
        Return Math.Max( a, b )
        
    End Function
    
    
    
    Public Function mini( ByVal a As Long, ByVal b As Long ) As Long
        
        Return Math.Min( a, b )
        
    End Function
    
    
    
    Public Function OperArray( ByVal fct As Func( Of Long, Long, Long ), ByVal arr As Long(), ByVal init As Long ) As Long()
        
        Dim n = arr.GetUpperBound( 0 )
        Dim ans( n ) As Long
        
        For i = 0 To n
            init = fct( init, arr( i ) )
            ans( i ) = init
        Next
        
        Return ans
        
    End Function
    
End Module
