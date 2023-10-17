from collections import Counter

def anagramFinder( words, queries ):
    
    words.sort()
    words_chars = [ Counter( word ) for word in words ]

    return [ [ words[i] for i in range( len( words ) ) if words_chars[i] == Counter( query ) ] for query in queries ]
