from collections import Counter

def firstNonRepeatingCharacter( str ):

    c = Counter( str )

    for ch in str:
        if c[ch] < 2:
            return ch

    return str[0]
