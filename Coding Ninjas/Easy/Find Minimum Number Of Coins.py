from typing import List

def MinimumCoins( n: int ) -> List[int]:
    c = [ 1000, 500, 100, 50, 20, 10, 5, 2, 1 ]
    ans = []
    d = 0

    for i in c:
        d, n = divmod( n, i )
        ans += [ i ] * d

    return ans
