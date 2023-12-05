Class Epidem
    
    
    
    Shared Function Epidemic( ByVal tm As Integer, ByVal n As Integer, ByVal s0 As Integer, ByVal i0 As Integer, ByVal b As Double, ByVal a As Double ) As Integer
        
        Dim dt = CDbl( tm / 336 )
        Dim st = CDbl( s0 )
        Dim it = CDbl( i0 )
        Dim i = it
        Dim r = it
        Dim max = it
        
        For p = 1 To n
            i = b * st * it * dt
            r = a * it * dt
            st -= i
            it += i - r
            max = Math.Max( max, it )
        Next
        
        Return Math.Floor( max )
        
    End Function



End Class
