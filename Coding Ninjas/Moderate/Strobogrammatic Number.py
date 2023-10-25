def isStrobogrammatic( n ):

    d = { "1": "1", "6": "9", "8": "8", "9": "6", "0": "0" }
    n = str( n )
    ans = ""

    for i in n[ : : -1 ]:
        if i not in d:
            return False

        ans += d[i]

    return ans == n
