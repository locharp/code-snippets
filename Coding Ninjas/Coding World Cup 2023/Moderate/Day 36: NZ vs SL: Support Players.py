from collections import *

def stringOperation( s: str, k: int ) -> str:

    c = Counter( s )
    t = sum( c.values() )
    s = 0

    for i in "aeiou":
        if i in c:
            if t - c[i] == k:
                return "YES"

            s = c[i]

    if s == 0 and t == k:
        return "YES"

    return "NO"
