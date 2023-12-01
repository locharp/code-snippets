Imports System.Collections.Generic
Imports System.Numerics

Public Module Kata
    
    Dim fibs As New List( Of BigInteger ) From { 0, 1 }
    Dim tris As New List( Of BigInteger ) From { 0, 0, 1 }
    Dim tets As New List( Of BigInteger ) From { 0, 0, 0, 1 }
    Dim pads As New List( Of BigInteger ) From { 1, 0, 0 }
    Dim jacs As New List( Of BigInteger ) From { 0, 1 }
    Dim pels As New List( Of BigInteger ) From { 0, 1 }
    
    
    
    Function Fibonacci( n As Integer ) As BigInteger
    
        If n < fibs.Count
            Return fibs( n )
        End If
        
        Return Fibonacci( n - 1 ) + Fibonacci( n - 2 )
        
    End Function
    
    
    
    Function Tribonacci( n As Integer ) As BigInteger
    
        If n < tris.Count
            Return tris( n )
        End If
        
        Return Tribonacci( n - 1 ) + Tribonacci( n - 2 ) + Tribonacci( n - 3 )
        
    End Function
    
    
    
    Function Tetranacci( n As Integer ) As BigInteger
    
        If n < tets.Count
            Return tets( n )
        End If
        
        Return Tetranacci( n - 1 ) + Tetranacci( n - 2 ) + Tetranacci( n - 3 ) + Tetranacci( n - 4 )
        
    End Function
    
    
    Function Padovan( n As Integer ) As BigInteger
        
        If n < pads.Count
            Return pads( n )
        End If
        
        Return Padovan( n - 1 ) + Padovan( n - 2 ) + Padovan( n - 3 )
        
    End Function
    
    
    
    Function Jacobsthal( n As Integer ) As BigInteger
    
        If n < jacs.Count
            Return jacs( n )
        End If
        
        Return Jacobsthal( n - 1 ) + ( 2 * Jacobsthal( n - 2 ) )
        
    End Function
    


    Function Pell( n As Integer ) As BigInteger
    
        If n < pels.Count
            Return pels( n )
        End If
        
        Return ( 2 * Pell( n - 1 ) ) + Pell( n - 2 )
        
    End Function
    
    
    
    Public Function Mixbonacci( pattern as String(), length as Integer ) As BigInteger()
        
        Dim ans( length - 1 ) As BigInteger
        Dim fib = 0, tri = 0, tet = 0
        Dim pad = 0, jac = 0, pel = 0
                                
        For i = 0 To length - 1
            Select Case pattern( i )
                Case "fib"
                    ans( i ) = Fibonacci( fib )
                    fib += 1
                Case "fib"
                    ans( i ) = Tribonacci( tri )
                    tri += 1
                Case "tet"
                    ans( i ) = Tetranacci( tet )
                    tet += 1
                Case "pad"
                    ans( i ) = Padovan( pad )
                    pad += 1
                Case "jac"
                    ans( i ) = Jacobsthal( jac )
                    jac += 1
                Case "pel"
                    ans( i ) = Pell( pel )
                    pel += 1
            End Select
        Next
        
        Return ans
                
    End Function
    
    
    
End Module 
