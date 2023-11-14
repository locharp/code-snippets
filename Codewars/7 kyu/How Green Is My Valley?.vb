Imports System

Public Module Valley
    
    
    
    Public Function MakeValley( ByVal arr As Integer() ) As Integer()
        
        Dim m = arr.Length Mod 2
        Dim p( ( arr.Length + 1 ) \ 2 - 1 ) As Integer
        Dim q( arr.Length \ 2 - 1 ) As Integer
        Array.Sort( arr )
        
        For i = 0 To p.Length - 1
            p( i ) = arr( i * 2 - m + 1 )
        Next
        
        For i = 0 To q.Length - 1
            q( i ) = arr( i * 2 + m )
        Next
        
        Return p.Reverse().ConCat( q ).ToArray()
        
    End Function
    
    
    
End Module



' Produce IndexOutOfRangeException on Codewars for unknown reason
Imports System

Public Module Valley
    
    
    
    Public Function MakeValley( ByVal arr As Integer() ) As Integer()
        
        Dim ans( arr.GetUpperBound(0) ) As Integer
        Dim m = arr.Length Mod 2
        Dim n = arr.Length \ 2
        Array.Sort( arr )
        ans( n ) = arr ( 0 )
        
        For i = 0 To n - 1
            ans( m + n + i ) = arr( m + i * 2 )
            ans( n - i - 1 ) = arr( m + i * 2 + 1 )
        Next
    
        Return ans
        
    End Function
    
    
    
End Module
