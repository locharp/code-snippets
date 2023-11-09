def minHours( a: list ) -> int:
    
    s = a[0]
    a = sorted( a[ 1 : ] )

    if s <= a[0]:
        return a[-1] - s
    elif s >= a[-1]:
        return s - a[0]
    else:
        return a[-1] - a[0] + min( a[-1] - s, s - a[0] )
