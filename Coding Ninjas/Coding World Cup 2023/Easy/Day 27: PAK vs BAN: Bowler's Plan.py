def kthUnique( n: int, s: str, k: int ) -> str:

    if k < 1:
        return "?"
        
    a = set()
    k -= 1

    for i in s:
        if i not in a:
            if len( a ) < k:
                a.add( i )
            else:
                return i

    return "?"
