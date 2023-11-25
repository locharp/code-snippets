Imports System
Imports System.Numerics

Public Module EasyLine



    Public Function EasyLine( ByVal n As Integer ) As BigInteger

        If n < 2
            Return n + 1
        End If

        Dim pt( n, n ) As BigInteger
        pt( 0, 0 ) = 1
        pt( 1, 0 ) = 1
        pt( 1, 1 ) = 1

        For i = 2 To n
            pt( i, 0 ) = 1
            pt( i, i ) = 1

            For j = 1 To i - 1
                pt( i, j ) = pt( i - 1, j - 1 ) + pt( i - 1, j )
            Next
        Next

        Dim ans As BigInteger

        For i = 0 To n
            ans += BigInteger.Pow( pt( n, i ), 2 )
        Next

        Return ans

    End Function



End Module
