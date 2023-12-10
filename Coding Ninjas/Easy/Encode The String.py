from string import ascii_lowercase

def encodeString(s: str, n: int) -> str:
    
    d = { ch: chr( ord( ch ) - 1 ) for ch in ascii_lowercase }
    
    for ch in "aeiou":
        d[ch] = chr( ord( ch ) + 1 )

    return "".join( d[ch] for ch in s )
