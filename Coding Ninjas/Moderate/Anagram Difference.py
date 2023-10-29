def getMinimumAnagramDifference( str1, str2 ):
    
    return sum( ( Counter( str1 ) - Counter( str2 ) ).va
