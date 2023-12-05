def timeTakenToMail( keyboard: str, s: str ) -> int:
    
    d = { j: i for i, j in enumerate( keyboard ) }
    ans = 0
    curr = 0

    for ch in s:
        ans += abs( curr - d[ch] )
        curr = d[ch]

    return ans
