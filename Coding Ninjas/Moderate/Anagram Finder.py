from collections import Counter

def anagramFinder( words, queries ):
    
    words.sort()
    words_chars = [ Counter( word ) for word in words ]
    ans = []

    for query in queries:
        q = Counter( query )
        ans.append( [] )

        for i in range( len( words ) ):
            if words_chars[i] == q:
                ans[-1].append( words[i] )

    return ans
