def kThCharaterOfDecryptedString( s, k ):
    
    c = i = o = 0

    while o < len( s ):
        if s[o].isdecimal():
            j = o

            while o < len( s ) and s[o].isdecimal():
                o += 1

            k -= ( j - i ) * int( s[ j : o ] )

            if k <= 0:
                return s[ j - ( k % ( j - i ) ) - 1 ]

            i = o

        o += 1
