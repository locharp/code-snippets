from collections import Counter

def is_anagram( test, original ):
    return Counter( test.upper() ) == Counter( original.upper() )