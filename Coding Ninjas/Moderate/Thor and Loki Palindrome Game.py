from collections import Counter

def thorAndLokiPalindromeGame( s: str ) -> str:

    ans = sum( i % 2 for i in Counter( s ).values() )

    if ans % 2 > 0:
        return "Thor"
    else:
        return "Loki"
