def  checkWordsInString( s, n, wordList ):
    
    return " ".join( str( word in s ) for word in wordList )
