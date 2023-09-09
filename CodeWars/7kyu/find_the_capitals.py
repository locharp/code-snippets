from string import ascii_uppercase

def capitals( word ):
    return [ i for i in range( len( word ) ) if word[i] in ascii_uppercase ]