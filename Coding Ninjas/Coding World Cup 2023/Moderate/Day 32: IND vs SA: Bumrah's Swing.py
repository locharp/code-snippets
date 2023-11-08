def maxVariation( n: int, a: list ) -> int:

    ans = 0
    s = set()
                
    for i in a:
        if i not in s:
            s.add( i )
            ans += 1 
        elif -i not in s:
            s.add( -i )
            ans += 1

    return ans 
